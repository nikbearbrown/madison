<!-- repo: https://github.com/nikbearbrown/homes-of-hope-plus-one | stars: 0 | updated: 2026-05-22T19:15:44Z -->

# Homes of Hope Plus One

**Author:** Nik Bear Brown
**Publisher:** Bear Brown, LLC
**Status:** Draft
**Started:** 2026-05-17

## Structure

```
book.md                 ← book description and high-level outline (planning)
outline.md              ← starter table of contents (planning)
vision.md               ← Tic TOC Phase 1: vision and positioning
architecture.md         ← Tic TOC Phase 2: learning architecture
chapters-spec.md        ← Tic TOC Phase 3: chapter specifications
risks.md                ← Tic TOC Phase 4: scope, market, risks
pantry/                 ← scratch storage for fragments, snippets, leftovers
chapters/
    00-frontmatter.md   ← copyright, dedication, preface
    01-introduction.md  ← Chapter 0 / Introduction
    02-chapter-01.md    ← Chapter 1
    ...
    04-chapter-03.md    ← Chapter 3
    99-back-matter.md   ← acknowledgments, about the author, notes, references, index
```

## Planning Documents

| File | Purpose |
|------|---------|
| `book.md` | One-sentence pitch, the argument, the gap, the reader, high-level outline. |
| `outline.md` | Chapter-level table of contents — keep in sync with `chapters/`. |
| `vision.md` | Tic TOC Phase 1 — book concept, type, learner profile, thesis, field positioning. |
| `architecture.md` | Tic TOC Phase 2 — learning outcomes, sequencing, three-act arc, prerequisites. |
| `chapters-spec.md` | Tic TOC Phase 3 — per-chapter specs, cases, contested claims, coverage gaps. |
| `risks.md` | Tic TOC Phase 4 — comparable texts, features, out of scope, adoption risks. |
| `pantry/` | Scratch storage for fragments and snippets that don't yet belong in a chapter. |

These files are for planning only. They are not compiled into the EPUB.

The four Tic TOC files are templated with `[NEEDS HUMAN INPUT]` markers
and a `*Phase N output from Tic TOC*` header signature. Run Tic TOC's
`/scaffold silent` to fill them from `book.md`, `outline.md`, `pantry/`,
and `chapters/`. Or build them section-by-section through the interactive
phase commands (`/i1` → `/m4`).

## Chapters

| File | Title | Status |
|------|-------|--------|
| 00-frontmatter.md | Front Matter (copyright, dedication, preface) | ☐ |
| 01-introduction.md | Introduction | ☐ |
| 02-chapter-01.md | Chapter 1 | ☐ |
| 03-chapter-02.md | Chapter 2 | ☐ |
| 04-chapter-03.md | Chapter 3 | ☐ |
| 99-back-matter.md | Back Matter (acknowledgments, notes, references, index) | ☐ |

## Build

```bash
./build.sh
```

Output goes to `output/` (gitignored).

## Figures

```bash
./graphs.sh
```

Processes `<!-- → [TYPE: description] -->` comments in every chapter:
- Tabular figures → classed markdown tables (`.infographic-table`, `.comparison-table`, `.data-table`)
- Non-tabular figures → placeholder images in `images/`, ready to replace
- CSS log appended to `styles/kindle-book.css` on each run

Review `chapters/*-updated.md`, then promote:
```bash
for f in chapters/*-updated.md; do mv "$f" "${f/-updated/}"; done
```

## Styles

| File | Purpose |
|------|---------|
| `styles/kindle.css` | Shared base — typography, figure table classes. Do not edit per book. |
| `styles/kindle-book.css` | Book-specific overrides. Edit freely. `graphs.sh` appends its log here. |

## Publish

Upload `output/homes-of-hope-plus-one.epub` to [KDP](https://kdp.amazon.com).

---

## What This Book Is

<!-- TODO: populate from chapter content -->

---

## Who This Book Is For

<!-- TODO: populate from chapter content -->

---

## How to Read It

<!-- TODO: populate from chapter content -->

---

## Table of Contents

| Chapter | Title | File |
|---------|-------|------|
| 1 | Unit 1 — Professional Register | [chapters/01-professional-register.md](chapters/01-professional-register.md) |
| 2 | Unit 2 — AI as Work Tool | [chapters/02-ai-as-work-tool.md](chapters/02-ai-as-work-tool.md) |
| 3 | Unit 3 — The CV | [chapters/03-the-cv.md](chapters/03-the-cv.md) |
| 4 | Unit 4 — The Job Search | [chapters/04-the-job-search.md](chapters/04-the-job-search.md) |
| 5 | Unit 5A — The Call Structure | [chapters/05a-the-call-structure.md](chapters/05a-the-call-structure.md) |
| 5 | Unit 5B — Medical Vocabulary Tier 1 | [chapters/05b-medical-vocabulary-tier-1.md](chapters/05b-medical-vocabulary-tier-1.md) |
| 5 | Unit 5C — Report and Proposal English | [chapters/05c-report-and-proposal-english.md](chapters/05c-report-and-proposal-english.md) |
| 6 | Unit 6A — Handling Difficult Calls | [chapters/06a-handling-difficult-calls.md](chapters/06a-handling-difficult-calls.md) |
| 6 | Unit 6B — Patient Communication | [chapters/06b-patient-communication.md](chapters/06b-patient-communication.md) |
| 6 | Unit 6C — Donor and Partner Communication | [chapters/06c-donor-and-partner-communication.md](chapters/06c-donor-and-partner-communication.md) |
| 7 | Unit 7A — The Phone Screen | [chapters/07a-the-phone-screen.md](chapters/07a-the-phone-screen.md) |
| 7 | Unit 7B — The Healthcare Interview | [chapters/07b-the-healthcare-interview.md](chapters/07b-the-healthcare-interview.md) |
| 7 | Unit 7C — The NGO Interview | [chapters/07c-the-ngo-interview.md](chapters/07c-the-ngo-interview.md) |
| 8 | Unit 8 — The Mock Interview | [chapters/08-the-mock-interview.md](chapters/08-the-mock-interview.md) |
| 9 | Unit 9 — The First Week | [chapters/09-the-first-week.md](chapters/09-the-first-week.md) |

---

## Signature Simulations

<!-- TODO: populate from chapter content -->

---

## Copyright

Copyright © 2026 Nik Bear Brown. All rights reserved.

Published by Bear Brown, LLC.

No part of this publication may be reproduced, distributed, or transmitted
in any form or by any means without the prior written permission of the
publisher, except in the case of brief quotations in critical reviews and
certain other noncommercial uses permitted by copyright law.

ISBN: [INSERT ISBN]

