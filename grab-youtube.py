#!/usr/bin/env python3
"""
grab-youtube.py — pull stats, transcripts, and (optionally) comments for a
YouTube channel, using yt-dlp. No API key or OAuth needed.

SETUP (one time):
    python3 -m pip install -U yt-dlp

USAGE:
    # metadata + transcripts for every video on a channel:
    python3 grab-youtube.py "https://www.youtube.com/@Musinique"
    python3 grab-youtube.py "https://www.youtube.com/@NikBearBrown"

    # cap the run, add comments (slow), or skip transcripts:
    python3 grab-youtube.py "https://www.youtube.com/@NikBearBrown" --max 50
    python3 grab-youtube.py "https://www.youtube.com/@Musinique" --comments --max-comments 100
    python3 grab-youtube.py "https://www.youtube.com/@NikBearBrown" --no-transcripts

OUTPUTS  (under <out>/<channel handle>/):
    channel.json            subscriber count, total views, video count
    videos.csv              one row/video: id, title, date, views, likes,
                            comments, duration, url, has_transcript
    transcripts/<id>.txt    plain-text transcript (auto or manual captions)
    comments/<id>.json      comment threads (only when --comments)

NOTES:
  - Subscriber counts YouTube shows are rounded (so ~70K, not an exact figure).
  - Comments are slow and heavily rate-limited by YouTube; default OFF. Use
    --comments to enable and --max-comments to cap per video.
  - The run is resumable: existing transcripts/metadata are skipped on rerun.
  - If YouTube throttles, rerun later — it picks up where it left off. You can
    also pass --sleep 2 to slow requests down.
"""

import argparse
import csv
import glob
import json
import os
import re
import sys
import time

try:
    import yt_dlp
except ImportError:
    sys.exit("yt-dlp not installed. Run:  python3 -m pip install -U yt-dlp")


def handle_from_url(url):
    m = re.search(r"@([A-Za-z0-9_.-]+)", url)
    if m:
        return m.group(1)
    return re.sub(r"\W+", "_", url.rstrip("/").split("/")[-1]) or "channel"


def list_video_ids(channel_url):
    """Flat-list every video id on the channel (cheap, one pass)."""
    opts = {"quiet": True, "extract_flat": True, "skip_download": True,
            "ignoreerrors": True}
    url = channel_url.rstrip("/")
    if not url.endswith("/videos"):
        url += "/videos"
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=False)
    entries = [e for e in (info.get("entries") or []) if e and e.get("id")]
    chan = {
        "channel": info.get("channel") or info.get("title"),
        "channel_id": info.get("channel_id"),
        "subscriber_count": info.get("channel_follower_count"),
        "video_count": len(entries),
        "channel_url": channel_url,
    }
    return [e["id"] for e in entries], chan


def json3_to_text(path):
    """Convert a yt-dlp json3 caption file to plain text."""
    try:
        data = json.load(open(path, encoding="utf-8"))
    except Exception:
        return None
    out = []
    for ev in data.get("events", []):
        for seg in ev.get("segs", []) or []:
            t = seg.get("utf8", "")
            if t and t != "\n":
                out.append(t)
    text = "".join(out)
    return re.sub(r"\s+\n", "\n", text).strip() or None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("channel", help="channel URL or @handle")
    ap.add_argument("--out", default="youtube")
    ap.add_argument("--max", type=int, default=0, help="limit number of videos (0 = all)")
    ap.add_argument("--comments", action="store_true", help="also fetch comments (slow)")
    ap.add_argument("--max-comments", type=int, default=100)
    ap.add_argument("--no-transcripts", action="store_true")
    ap.add_argument("--sleep", type=float, default=0.0, help="seconds between videos")
    args = ap.parse_args()

    chan_url = args.channel
    if chan_url.startswith("@"):
        chan_url = "https://www.youtube.com/" + chan_url
    handle = handle_from_url(chan_url)

    base = os.path.join(args.out, handle)
    tdir = os.path.join(base, "transcripts")
    cdir = os.path.join(base, "comments")
    os.makedirs(tdir, exist_ok=True)
    if args.comments:
        os.makedirs(cdir, exist_ok=True)

    print(f"Listing videos for @{handle} ...")
    ids, chan = list_video_ids(chan_url)
    if args.max:
        ids = ids[: args.max]
    subs = chan.get("subscriber_count")
    print(f"Channel: {chan.get('channel')} | subscribers: {subs} | videos found: {chan['video_count']}")
    print(f"Processing {len(ids)} videos.\n")

    rows = []
    for i, vid in enumerate(ids, 1):
        vurl = f"https://www.youtube.com/watch?v={vid}"
        tpath = os.path.join(tdir, f"{vid}.txt")
        has_t = os.path.exists(tpath)

        opts = {
            "quiet": True, "skip_download": True, "ignoreerrors": True,
            "writeautomaticsub": not args.no_transcripts and not has_t,
            "writesubtitles": not args.no_transcripts and not has_t,
            "subtitleslangs": ["en", "en-US", "en-orig"],
            "subtitlesformat": "json3",
            "outtmpl": os.path.join(tdir, "%(id)s.%(ext)s"),
            "getcomments": args.comments,
        }
        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(vurl, download=not (args.no_transcripts or has_t))
        except Exception as e:
            print(f"[{i}/{len(ids)}] {vid} — ERROR: {e}")
            continue
        if info is None:
            print(f"[{i}/{len(ids)}] {vid} — unavailable")
            continue

        # transcript: convert any json3 we just wrote, then clean up
        if not has_t and not args.no_transcripts:
            j3 = glob.glob(os.path.join(tdir, f"{vid}*.json3"))
            txt = json3_to_text(j3[0]) if j3 else None
            for f in j3:
                try: os.remove(f)
                except OSError: pass
            if txt:
                open(tpath, "w", encoding="utf-8").write(txt)
                has_t = True

        # comments
        n_comments = info.get("comment_count")
        if args.comments:
            cs = (info.get("comments") or [])[: args.max_comments]
            json.dump(cs, open(os.path.join(cdir, f"{vid}.json"), "w", encoding="utf-8"),
                      ensure_ascii=False, indent=1)

        rows.append({
            "id": vid,
            "title": info.get("title", ""),
            "upload_date": info.get("upload_date", ""),
            "views": info.get("view_count"),
            "likes": info.get("like_count"),
            "comments": n_comments,
            "duration_s": info.get("duration"),
            "url": vurl,
            "has_transcript": has_t,
        })
        print(f"[{i}/{len(ids)}] {info.get('title','')[:60]} — "
              f"views={info.get('view_count')} transcript={'Y' if has_t else 'n'}")
        if args.sleep:
            time.sleep(args.sleep)

    # capture exact subscriber count from a video if channel-level was blank
    if subs is None and rows:
        chan["subscriber_count"] = info.get("channel_follower_count")
    json.dump(chan, open(os.path.join(base, "channel.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

    if rows:
        with open(os.path.join(base, "videos.csv"), "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader(); w.writerows(rows)

    n_t = sum(1 for r in rows if r["has_transcript"])
    total_views = sum(r["views"] or 0 for r in rows)
    print(f"\nDone @{handle}: {len(rows)} videos, {n_t} transcripts, "
          f"{total_views:,} total views across pulled videos.")
    print(f"  -> {base}/  (channel.json, videos.csv, transcripts/" +
          (", comments/" if args.comments else "") + ")")


if __name__ == "__main__":
    main()
