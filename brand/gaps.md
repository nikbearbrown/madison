# gaps.md — the delta between my attested record and what my aspiration demands

My aspiration (brand.yml): a **full-stack & mobile SWE who ships AI-powered product features
end to end**, seen by **recruiters/hiring managers (primary)** and **AI-first founders (secondary)**.
Below: each thing the target demands that my `resume.json` does **not** yet prove. Column 4 is the
point of this exercise — the **Madison build** whose construction *is* the closing of the gap.

**The migration rule (runs all semester):** a gap closes only with evidence (the build shipped /
the artifact published to its target medium) → the evidence becomes a new attested `resume.json`
entry → the gap row is **deleted**. This file is a place things leave.

## The delta

| # | Gap | Evidence the target demands it | What I have today | Madison build that closes it | Plan |
|---|---|---|---|---|---|
| **1 (TOP — project proposal)** | **No public, verifiable proof of the lead attribute.** "Ships full-stack + a real AI layer" is true, but the proof is private (Savor/BlueBox company work) or unlinked (project repos have no URL, portfolio is a brochure, not case studies). | Step 3: engineering audiences read GitHub + runnable case studies (SimplifyJobs/jobright feeds run on GitHub; founders reward demos over skill lists). [Stack Overflow 2024; SimplifyJobs] | `resume.json` projects exist but `repo`/`live_url` are null/`[TODO]`; portfolio site exists but has no case studies; GitHub handle not even captured. | **Ship the Live Website Accessibility Monitor (Assignment 1 Part 2)** as a public, runnable product — reusing my own `kanishk-singh-accessibility-standards-monitor-and-site-audit-reports` recipe and publishing it as a case study via `madison-brand-portfolio-dashboard` (public repo + live demo + measured WCAG outcomes). It IS the lead-attribute proof: a full-stack build (Playwright crawler + scan-diffing + score-timeline dashboard) with a real AI layer (Claude fix-suggestions). | Ship the monitor this semester (crawler → WCAG audit → scan-diff timeline → Claude fixes); publish repo + live demo + one measured outcome → folds into a new attested `resume.json` entry → delete this row. Then the Savor AI-search + voice-analytics case studies. |
| 2 | **Interview-screen readiness is unproven.** DSA/system-design is the gate before any human reads my résumé. | Step 3: new-grad funnels open with an online assessment, then onsites (Google process). [Glassdoor; HackerRank] | No record of OA pass-rate or mock-interview outcomes; brand.yml correctly keeps this OUT of unique_attributes. | **Adapt `madison-performance-reporting`** into a personal assessment-readiness dashboard: log practice sets, mock-interview verdicts, and real OA outcomes as a verified track record. | Maintain the log to the first cleared on-site; a real OA pass becomes an attestable signal, not a row here. |
| 3 | **I don't know where the live new-grad reqs are, so I apply late.** Discovery is ad hoc. | Step 3: community GitHub aggregators surface fresh 2026 new-grad reqs in near-real-time; early applicants win. [SimplifyJobs; jobright-ai] | Manual, scattered job search; no monitored feed keyed to "full-stack/mobile new-grad SWE." | **Extend `cloud-platform-release-and-jobs-monitor` (cf. `denis-bykov-job-market-intelligence`)** into a new-grad-SWE job-signal monitor: pull + dedupe the aggregator feeds, filter to my aspiration, emit a verified daily shortlist + an application/referral tracker. | Build the monitor; it's itself a shipped public tool → folds into Gap 1's portfolio as a 4th case study. |
| 4 | **No public AI-engineering voice** for the secondary (founder) audience. | brand.yml SECONDARY audience rewards a teachable write-up of shipped work. [inference] | Zero published technical writing; one-line LinkedIn summary only. | **Extend `content-agent` / `madison-copy-content-generation`** to turn one shipped feature (Savor's MCP context-retrieval) into a verified-claims technical post. | One post mapped to a real artifact; abandon if it competes with Gaps 1–3 for time. |
| ~~5~~ | ~~Grow LinkedIn following / be active on social to build a personal brand.~~ | ~~"Be active online."~~ | ~~~3 connections short of nothing in particular~~ | ~~A social-posting cadence recipe~~ | **KILLED — wrong row.** For a new-grad SWE, follower count is the `_excluded_drift` vanity metric, not a hire signal; referrals + screens + campus pipelines decide outcomes (brand.yml `media_cut`). This is the exact round-one trap the exercise warns against, so it's not a gap — it's a distraction. [Pinpoint; SHRM] |

### Foundational credibility gaps (a "shipping engineer" brand can't have dead links)

| Gap | Source | Action |
|---|---|---|
| ~~GitHub handle not even captured~~ | `resume.json` issues_open[B] | **RESOLVED 2026-06-22** — handle captured (`github.com/Kanishk0507`). Residual ("pin the proof repos") folds into Gap 1. |
| ~~BTech dropped from the SDE résumé / dates looked off~~ | `resume.json` import-error #3 + issues_open[A] | **RESOLVED 2026-06-22** — dates confirmed real (break + industry work during the degree); degree restored to `resume.json`. Residual: add it back to the SDE résumé doc itself (external file). |

### One row, rewritten in my own words (rubric line 10)

> **Gap 1, my version:** My best evidence is locked up. The work I'm proudest of — the semantic
> search and MCP backend at Savor, five shipped Flutter apps — lives behind a company NDA or in
> repos I never made public, and my "portfolio" is really just a landing page. So when a hiring
> manager Googles me, the proof that I actually ship doesn't exist where they look. The fix isn't
> to *say* it louder in `brand.yml`; it's to **build the public artifacts that make it checkable**,
> let them land in `resume.json`, and only then claim them. I'd rather have three repos a stranger
> can clone than three more adjectives.

---

## Assignment 1 Part 2 — Project proposal (this IS my submitted Part 2)

**Live Website Accessibility Monitor — the Madison build that proves what I claim**

I will build a continuous accessibility-monitoring platform that crawls registered websites weekly,
audits every page against WCAG 2.1 success criteria (Levels A, AA, AAA), and tracks violations over
time. Most accessibility audits are one-time snapshots; this shifts accessibility into a living,
continuous quality signal. The system diffs each scan against the prior one to surface newly
introduced regressions, resolved issues, and score trends, then sends automated change reports
(email or dashboard) with a visual score timeline per site and page. Core checks include color
contrast, missing ARIA roles, broken keyboard navigation, unlabeled form fields, improper heading
hierarchy, and missing alt text. The Claude API generates plain-language explanations and specific
code fixes per violation. For organizations under ADA, Section 508, or the European Accessibility
Act it provides an auditable compliance history; for marketing teams — the heaviest publishers of
web content — it catches regressions before launch. On Madison it reuses the accessibility/site-audit
recipe I already authored, so per the migration rule a shipped, published monitor becomes a new
attested `resume.json` entry — and Gap 1 gets deleted, not edited.

*(Word count: ~185.)*
