# Board reconciliation — Assignment 1 Figma board vs. brand/ artifacts

**What this is:** my Assignment 1 Figma board was built *before* these `brand/` files existed, so it's
the **report** and `brand/` is the **truth** it should render. This pass does one thing (per Exercise 1,
Step 5): every claim on the board either gets a **pointer to the `brand/` file that backs it**, or gets
**flagged `[UNTRACEABLE]`**. I do **not** fix the board yet — I only flag. Exercise 1A automates this check;
today's `[UNTRACEABLE]` rows become its first test data.

## Snapshot (action for me)

Board snapshot CAPTURED and committed (2026-06-22) — all four parts, clear and readable:

- **Board link:** https://www.figma.com/board/wJCg5OaVI62Eg4cmBYm994/INFO-7375?node-id=0-1 (Figma, INFO 7375 board)
- **Snapshot files (in `brand/`):**
  - `board-snapshot-2026-06-22-part1a-1b.png` — Part 1A professional intro + Part 1B skills inventory
  - `board-snapshot-2026-06-22-part2.png` — Part 2 Live Website Accessibility Monitor proposal
  - `board-snapshot-2026-06-22-part3.png` — Part 3 brand baseline (doubles as the LinkedIn baseline capture)
  - `board-snapshot-2026-06-22-part4.png` — Part 4 essential tools setup
- **Status:** this is a **snapshot** — accurate at capture (2026-06-22), drifts the moment a gap closes or a résumé entry lands.

## Claim-by-claim trace

> Traced against the **real** board (the compressed Assignment 1 PDF, reviewed 2026-06-22), not a
> guess. A claim with **no backing file** is decoration posing as evidence — flagged below.

| Board claim (from the Assignment 1 deck) | On the board? | Traces to brand/ artifact | Verdict |
|---|---|---|---|
| Part 1A intro: name, "MSIS 2026 @ Northeastern," full-stack/mobile SWE, links | YES | `resume.json` identity + `brand.yml` aspiration | TRACED |
| Part 1A career vision: "Senior/Staff SWE at a top product company, AI-native systems" | YES | `brand.yml` aspiration (near-term framing of the same trajectory) | TRACED |
| Part 1B market evidence: 5 postings (Google·Meta·Stripe·Atlassian·HubSpot, May 2025) | YES | `brand.yml` → audience.postings_reviewed (now filled from the board) | TRACED |
| Part 1B self-ratings (3.5 / 2 / 4.5 / 3 across AI · design · technical · professional) | YES | `private-reflection.md` (durable per-skill ratings live there, gitignored) | TRACED — granularity differs; see finding #3 |
| Part 2 project: **Live Website Accessibility Monitor** (full proposal) | YES | `gaps.md` → "Assignment 1 Part 2 — Project proposal" + Gap 1 build | **TRACED (after fix — see finding #1)** |
| Part 3 baseline: portfolio live, 10 GitHub repos, LinkedIn custom URL | YES | `resume.json` → identity.links | TRACED |
| Part 3 admitted inconsistency: GitHub bio "passionate student" vs résumé "Software Engineer" | YES | `gaps.md` — cross-platform consistency | **FLAG → see finding #2** |
| Work-experience metrics ("40% faster," "35% latency," "95% downtime cut") | YES | `resume.json` highlights, with [cv]/[li] source labels | TRACED to labeled entries |
| BlueBox title / LinkedIn headline on the board | YES — LI headline shows "Mobile Application Developer"; no stale "Jr. Flutter Developer" anywhere | `resume.json` import-error #2 — canonical "Mobile Application Developer" | **TRACED — consistent, flag cleared** |
| LinkedIn follower/connection count ("5,160 followers · 500+ connections") | YES — on the Part 3 LinkedIn screenshot | `resume.json` `_excluded_drift` (deliberately excluded) | **`[UNTRACEABLE]` by design** — vanity metric, never enters the durable record |

## `[UNTRACEABLE]` / FLAG log (Exercise 1A's first test data)

Found by reconciling the **real** board against `brand/` on 2026-06-22:

1. **Part 2 project mismatch — FOUND & FIXED.** The board's Assignment 1 Part 2 is the **Live
   Website Accessibility Monitor**, but `gaps.md` had drafted a *different* Part 2 ("Attested
   Case-Study Portfolio Pipeline") because these files were built before I'd seen the board. The
   board is the submitted assignment, so `gaps.md` was reconciled to match it — Gap 1's build cell
   and the Part 2 proposal now both describe the Accessibility Monitor. This is exactly the
   report-vs-truth drift Step 5 exists to catch.
2. **GitHub bio inconsistency — FLAG, confirmed on the board (not fixed today).** The board's own
   Part 3 "areas for enhancement" says it: the GitHub bio reads "passionate student" while the
   résumé reads "Software Engineer." A real cross-platform-consistency gap; fix on GitHub or promote
   it to a `gaps.md` row.
3. **Self-ratings granularity — confirmed.** The board publishes category-level self-ratings
   (AI 3.5 / Design 2 / Technical 4.5 / Professional 3); the durable, per-skill honest ratings live
   in `private-reflection.md` (gitignored). Different scope, not a contradiction — but don't let the
   public board number stand in for the private one.
4. **Vanity metric present — `[UNTRACEABLE]` by design.** The Part 3 LinkedIn screenshot shows
   "5,160 followers · 500+ connections" — exactly the `_excluded_drift` class (true today, stale next
   week). It stays OUT of `resume.json`. No other untraceable claims surfaced on the reviewed parts (1A–3).

**Rule going forward:** an `[UNTRACEABLE]` claim gets *one* of two fates later — add the backing file
(promote a `gaps.md` row once its evidence lands) or cut the claim.
