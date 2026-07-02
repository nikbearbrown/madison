<!-- repo: https://github.com/nikbearbrown/ai-driven-programmatic-hcp-marketing | stars: 0 | updated: 2026-06-17T16:18:12Z -->

# AI-Driven Programmatic HCP Marketing

*Targeting, Evidence, and the External Innovation Lab*
**Humanitarians AI and Nik Bear Brown** · Irreducibly Human / The AI+1 Series

## What this is

A field manual for seeing the AI-driven HCP (healthcare-provider) marketing machine clearly and grading its claims honestly. Pharmaceutical marketing has built a fast, precise, AI-driven machine for *engaging* physicians — NPI targeting, point-of-care delivery inside the EHR, next-best-action engines — and almost no discipline for proving that the engagement *caused* a prescription worth causing. This book gives you the vocabulary (lift vs. brand, attribution circularity, the Evidence Ladder, the IP firewall) and the method to tell mechanism from effect, association from cause, and a tuned baseline from a routed model that supposedly beats it. Its central argument: the script-lift figures that drive HCP budgets are associations systematically inflated by selection, attribution circularity, missing controls, and reporting bias — and the most valuable AI work is not producing a better number but specifying the design that would make a number trustworthy.

## Who it's for

The data-capable Fellow and the marketing-science team working alongside a martech partner — people who can read a model, join a public dataset, and are responsible for telling a brand team what the evidence does and does not support. It assumes basic statistics and a little code; it builds causal inference from the ground up. It is **not** legal/compliance counsel, a deep-learning course, or a media-buying handbook.

## The innovation-lab offer

Bear Brown, LLC and Humanitarians AI together operate as an **external innovation lab**. We research and prototype the AI that *might* help a company — scope the question, build a proof of concept on public or synthetic data, test whether it holds — and then work alongside the company's own team to implement what proves promising. Humanitarians AI runs 100–200 Fellows at any time across many majors, so extra hands can be staffed on a per-hour basis for a few weeks. The contract that makes it safe is an **IP firewall**: published work uses public/synthetic data only; the partner replicates promising methods on its proprietary data, internally. Low commitment for the company, high evidence for the decision. **This book is that lab's method written down** — Chapters 11–14 are the operating model, research design, portfolio, and handoff brief. Running the exercises is a preview of working with the lab.

## Chapters

| # | Title |
|---|---|
| 00 | Front Matter · Introduction |
| 1 | The Machine Nobody Sees |
| 2 | Lift vs. Brand: The Two Dependent Variables |
| 3 | The HCP Identity Graph and the Targeting Data |
| 4 | What Today's AI Stack Actually Does (and Claims) |
| 5 | The Evidence Problem |
| 6 | Ensembles and the Tabular-Data Advantage |
| 7 | Mixture of Experts and Related Routing Models (and When the Word Is Marketing) |
| 8 | Uplift and Incrementality: Measuring Real Lift |
| 9 | Brand Association as a Measurable Outcome |
| 10 | LLMs for Commercial Research and Content Intelligence |
| 11 | The External Innovation Lab Operating Model (and the IP Firewall) |
| 12 | Research Design and Public Data for Marketing Science |
| 13 | The Fellow Research Portfolio (Run One) |
| 14 | From Prototype to Product Decision (The Fellow's Brief) |
| 99 | Back Matter |

## How the repo is used (learn by doing)

```
chapters/   ← markdown source, one file per chapter
images/     ← static SVG + PNG figures used by the EPUB
d3/         ← interactive D3 HTML versions of each figure (browser-runnable)
SCRIPTS/    ← svg-to-png.mjs and build helpers
```

The book is built around **public and synthetic data**, so every method is one you can actually run. Each chapter ends with a five-part exercise block — *When to Use AI*, *When NOT to Use AI*, an LLM exercise, a CLI exercise, and an AI-validation exercise — that builds a running project, **One Drug, End to End**: pick a single branded drug in Chapter 1 and carry it through every chapter, from split-agency map to a one-page partner handoff brief. Each chapter also includes ready-to-paste **Prompts** for recreating its figures.

Build (Kindle/EPUB):

```bash
npm install        # first time only
./build.sh         # output → output/ (gitignored)
node SCRIPTS/svg-to-png.mjs   # regenerate PNGs from SVG
```

## About Humanitarians AI & Bear Brown, LLC

**Humanitarians AI** is a 501(c)(3) nonprofit (EIN 33-1984805), founded in 2019 in Boston. Its Fellows Program connects data-capable people to real projects, mentors, and the *Irreducibly Human* curriculum, and the Fellows wrote and ran the case studies in this book. **Bear Brown, LLC** and Humanitarians AI together run the external innovation lab this book describes.

[humanitarians.ai](https://www.humanitarians.ai/) · [bearbrown.co](https://www.bearbrown.co/) · [info@humanitarians.ai](mailto:info@humanitarians.ai)

## Copyright

Copyright © 2026 Humanitarians AI and Nik Bear Brown. All rights reserved. Published by Bear Brown, LLC, in partnership with Humanitarians AI, a 501(c)(3) nonprofit organization. See [LICENSE.md](LICENSE.md).

## Medhavy

These are Kindle / online editions, designed for integration with **Medhavy** (also **Medhavi**) — मेधावी, Sanskrit for "intelligent" — an AI-native intelligent-textbook system at [medhavy.com](https://www.medhavy.com/). In Medhavy the chapters become adaptive practice: hints, worked examples, quizzes, and feedback loops. Come learn something with us.
