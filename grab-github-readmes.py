#!/usr/bin/env python3
"""
grab-github-readmes.py — download the README from every repo for a GitHub user.

Usage:
    export GITHUB_TOKEN=ghp_xxx          # strongly recommended (see notes)
    python3 grab-github-readmes.py                      # defaults to nikbearbrown
    python3 grab-github-readmes.py --user someuser --out readmes
    python3 grab-github-readmes.py --include-forks --include-archived

Outputs:
    <out>/<repo-name>.md     one README per repo (skips repos with none)
    <out>/_index.csv         repo, description, stars, fork, archived, has_readme, url, updated
    <out>/_no_readme.txt     repos that had no README

Notes on the token (why you want one):
  - Unauthenticated GitHub API = 60 requests/hour. 400 repos = ~404 requests,
    so you'd get rate-limited almost immediately.
  - A token (even a no-scope "public_repo" classic token, or a fine-grained
    read-only one) gives 5,000 req/hour — plenty.
  - A token is also REQUIRED to see your own private repos. Without it you
    only get public ones.
  - Make one at: https://github.com/settings/tokens  (scope: public_repo, or
    repo if you want private READMEs too). Never commit the token.

The script is resumable: rerun it and it skips READMEs already on disk.
"""

import argparse
import base64
import csv
import os
import sys
import time
import urllib.request
import urllib.error

API = "https://api.github.com"


def gh(url, token):
    """GET a GitHub API URL, returning (json-or-bytes, response-headers)."""
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "grab-github-readmes")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req) as r:
            return r.read(), dict(r.headers)
    except urllib.error.HTTPError as e:
        return e, dict(e.headers)


def respect_rate_limit(headers):
    """If we're nearly out of API budget, sleep until the window resets."""
    try:
        remaining = int(headers.get("X-RateLimit-Remaining", "1"))
    except ValueError:
        return
    if remaining <= 2:
        reset = int(headers.get("X-RateLimit-Reset", str(int(time.time()) + 60)))
        wait = max(reset - int(time.time()), 0) + 2
        print(f"  ! rate limit low, sleeping {wait}s until reset...")
        time.sleep(wait)


def _paginate(base_url, token, include_forks, include_archived):
    import json
    repos, page = [], 1
    sep = "&" if "?" in base_url else "?"
    while True:
        url = f"{base_url}{sep}per_page=100&page={page}"
        body, headers = gh(url, token)
        if isinstance(body, urllib.error.HTTPError):
            print(f"ERROR listing repos (HTTP {body.code}): {body.read().decode()[:200]}")
            sys.exit(1)
        batch = json.loads(body)
        if not batch:
            break
        for r in batch:
            if r.get("fork") and not include_forks:
                continue
            if r.get("archived") and not include_archived:
                continue
            repos.append(r)
        respect_rate_limit(headers)
        page += 1
    return repos


def list_repos(user, token, include_forks, include_archived, public_only):
    """
    With a token (default): use the authenticated /user/repos endpoint with
    affiliation=owner,collaborator,organization_member + visibility=all, which
    returns your PRIVATE repos and repos in ORGS you belong to (Humanitarians AI,
    AI Skunkworks, course orgs, etc.) — not just your 96 public ones.

    Without a token, or with --public-only, fall back to /users/<user>/repos,
    which is public-repos-only.
    """
    if token and not public_only:
        url = (f"{API}/user/repos?sort=updated"
               "&affiliation=owner,collaborator,organization_member&visibility=all")
        repos = _paginate(url, token, include_forks, include_archived)
        # de-dupe by full_name (a repo can match multiple affiliations)
        seen, uniq = set(), []
        for r in repos:
            fn = r.get("full_name") or r["name"]
            if fn not in seen:
                seen.add(fn)
                uniq.append(r)
        return uniq
    url = f"{API}/users/{user}/repos?sort=updated"
    return _paginate(url, token, include_forks, include_archived)


def get_readme(owner, repo, token):
    import json
    body, headers = gh(f"{API}/repos/{owner}/{repo}/readme", token)
    respect_rate_limit(headers)
    if isinstance(body, urllib.error.HTTPError):
        return None  # 404 = no README
    data = json.loads(body)
    if data.get("encoding") == "base64":
        return base64.b64decode(data["content"]).decode("utf-8", errors="replace")
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--user", default="nikbearbrown")
    ap.add_argument("--out", default="readmes")
    ap.add_argument("--include-forks", action="store_true")
    ap.add_argument("--include-archived", action="store_true")
    ap.add_argument("--public-only", action="store_true",
                    help="only this user's public repos (the 96), skip private/org repos")
    args = ap.parse_args()

    token = os.environ.get("GITHUB_TOKEN", "").strip()
    public_only = args.public_only
    if not token:
        print("WARNING: no GITHUB_TOKEN set — 60 req/hr limit, PUBLIC repos only "
              "(your 96). Set a token to reach private + org repos.\n")

    os.makedirs(args.out, exist_ok=True)

    scope = "public only" if (public_only or not token) else "all (owner + private + orgs)"
    print(f"Listing repos for '{args.user}' [{scope}]...")
    repos = list_repos(args.user, token, args.include_forks, args.include_archived, public_only)
    print(f"Found {len(repos)} repos to process.\n")

    index_rows, no_readme = [], []
    for i, r in enumerate(repos, 1):
        owner = (r.get("owner") or {}).get("login", args.user)
        name = r["name"]
        full = r.get("full_name", f"{owner}/{name}")
        # filename = owner__repo, so same-named repos in different orgs don't collide
        safe = full.replace("/", "__")
        dest = os.path.join(args.out, f"{safe}.md")
        has_readme = False

        if os.path.exists(dest):
            has_readme = True
            print(f"[{i}/{len(repos)}] {full} — already downloaded, skipping")
        else:
            text = get_readme(owner, name, token)
            if text is None:
                no_readme.append(full)
                print(f"[{i}/{len(repos)}] {full} — no README")
            else:
                header = (f"<!-- repo: {r['html_url']} | "
                          f"private: {r.get('private', False)} | "
                          f"stars: {r.get('stargazers_count', 0)} | "
                          f"updated: {r.get('updated_at', '')} -->\n\n")
                with open(dest, "w", encoding="utf-8") as f:
                    f.write(header + text)
                has_readme = True
                print(f"[{i}/{len(repos)}] {full} — saved ({len(text)} chars)")

        index_rows.append({
            "full_name": full,
            "owner": owner,
            "repo": name,
            "private": r.get("private", False),
            "description": (r.get("description") or "").replace("\n", " "),
            "stars": r.get("stargazers_count", 0),
            "fork": r.get("fork", False),
            "archived": r.get("archived", False),
            "has_readme": has_readme,
            "url": r["html_url"],
            "updated": r.get("updated_at", ""),
        })

    with open(os.path.join(args.out, "_index.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(index_rows[0].keys()))
        w.writeheader()
        w.writerows(index_rows)

    if no_readme:
        with open(os.path.join(args.out, "_no_readme.txt"), "w", encoding="utf-8") as f:
            f.write("\n".join(no_readme) + "\n")

    saved = sum(1 for r in index_rows if r["has_readme"])
    print(f"\nDone. {saved}/{len(repos)} repos had a README.")
    print(f"  READMEs:   {args.out}/<repo>.md")
    print(f"  Index:     {args.out}/_index.csv")
    if no_readme:
        print(f"  No README: {args.out}/_no_readme.txt  ({len(no_readme)} repos)")


if __name__ == "__main__":
    main()
