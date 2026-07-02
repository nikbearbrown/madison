#!/usr/bin/env python3
"""
list-repos.py — print the NAME of every repo you can see (public + private + org).
Names only. No cloning, no README download.

    python3 list-repos.py          # uses your existing auth, no token pasting

Token resolution order (uses whatever the machine already has):
    1. $GITHUB_TOKEN if set
    2. `gh auth token`  (GitHub CLI — if you've run `gh auth login`)
Writes the list to repo-names.txt and prints it. Paste the relevant ones back.
"""
import json, os, sys, subprocess, urllib.request, urllib.error

API = "https://api.github.com"

def _from_gh_cli():
    try:
        return subprocess.check_output(["gh", "auth", "token"],
                                       stderr=subprocess.DEVNULL).decode().strip()
    except Exception:
        return ""

def _from_git_credential():
    """Pull the same token your `git clone` already uses (macOS keychain, etc.)."""
    try:
        p = subprocess.run(["git", "credential", "fill"],
                           input="protocol=https\nhost=github.com\n\n",
                           capture_output=True, text=True, timeout=10)
        for line in p.stdout.splitlines():
            if line.startswith("password="):
                return line.split("=", 1)[1].strip()
    except Exception:
        pass
    return ""

def resolve_token():
    for src in (os.environ.get("GITHUB_TOKEN", "").strip(),
                _from_gh_cli(), _from_git_credential()):
        if src:
            return src
    sys.exit("No GitHub auth found via env, gh, or git credential helper.")

token = resolve_token()

def get(url):
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "list-repos",
    })
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

repos, page = [], 1
while True:
    batch = get(f"{API}/user/repos?per_page=100&page={page}"
                "&affiliation=owner,collaborator,organization_member&visibility=all")
    if not batch:
        break
    repos.extend(batch)
    page += 1

# de-dupe + sort
seen, rows = set(), []
for r in repos:
    fn = r["full_name"]
    if fn in seen:
        continue
    seen.add(fn)
    rows.append((fn, "private" if r.get("private") else "public"))
rows.sort()

lines = [f"{vis:7}  {fn}" for fn, vis in rows]
out = "\n".join(lines)
with open("repo-names.txt", "w", encoding="utf-8") as f:
    f.write(out + "\n")

print(out)
print(f"\n{len(rows)} repos total "
      f"({sum(1 for _, v in rows if v=='private')} private, "
      f"{sum(1 for _, v in rows if v=='public')} public)")
print("Written to repo-names.txt")
