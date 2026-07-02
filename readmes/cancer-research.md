<!-- repo: https://github.com/nikbearbrown/cancer-research | stars: 0 | updated: 2026-06-09T02:34:31Z -->

# Cancer Research

**Author:** Humanitarians AI Incorporated
**Publisher:** Humanitarians AI Incorporated
**Status:** Draft
**Started:** 2026-06-08

## Structure

```
book.md                 ← book description and high-level outline
outline.md              ← chapter-level TOC
vision.md               ← Tic TOC Phase 1
architecture.md         ← Tic TOC Phase 2
chapters-spec.md        ← Tic TOC Phase 3
risks.md                ← Tic TOC Phase 4
pantry/                 ← scratch fragments
chapters/               ← markdown source files
images/                 ← PNGs used by the EPUB
d3/                     ← interactive D3 HTML figures

— Extraction directories (populated by Cowork extraction pass) —
anki/                   ← Key Terms → Anki import files
wayback/                ← AI Wayback Machine sections
when-to-use-ai/         ← Exercise 1 & 2 (judgment frame) blocks
llm/                    ← Exercise 3 LLM Exercise blocks
cli/                    ← Exercise 4 CLI Exercise blocks
ai-validation/          ← Exercise 5 AI Validation blocks
exercises/              ← Exercises sections
bridge/                 ← Bridge sections
assessments/            ← Assessments sections
further-reading/        ← Further Reading sections
cli-quick-reference/    ← CLI Quick Reference sections

— Supplemental learning mode directories (instructor-populated) —
glimmers/               ← Glimmer generative assignments
rubrics/                ← Grading rubrics for Glimmer and case studies
lecture-notes/          ← Slide-ready condensed chapter summaries
worked-problems/        ← Step-by-step solved examples
quizzes/                ← Platform quiz files
exams/                  ← Exam banks
discussion-prompts/     ← Seminar-style discussion questions
case-studies/           ← Case study scenarios (professor-authored only)
supplemental/           ← Optional ala carte chapters + catalog.md
slides/                 ← Presentation slides (see also)
videos/                 ← Video scripts or links (see also)

SCRIPTS/
    svg-to-png.mjs      ← converts images/**/*.svg to 300dpi PNG
```

## Chapter Progress

| File | Title | Draft | anki | wayback | when-to-use-ai | llm | cli | ai-validation | exercises | bridge | assessments | further-reading | cli-quick-ref | glimmer | quiz |
|------|-------|-------|------|---------|----------------|-----|-----|---------------|-----------|--------|-------------|-----------------|---------------|---------|------|
| 00-frontmatter.md | Front Matter | ☐ | — | — | — | — | — | — | — | — | — | — | — | — | — |
| 01-introduction.md | Introduction | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| 02-chapter-01.md | Chapter 1 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| 03-chapter-02.md | Chapter 2 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| 04-chapter-03.md | Chapter 3 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| 05-chapter-04.md | Chapter 4 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| 06-chapter-05.md | Chapter 5 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| 07-chapter-06.md | Chapter 6 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| 08-chapter-07.md | Chapter 7 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| 09-chapter-08.md | Chapter 8 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| 10-chapter-09.md | Chapter 9 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| 11-chapter-10.md | Chapter 10 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| 12-chapter-11.md | Chapter 11 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| 99-back-matter.md | Back Matter | ☐ | — | — | — | — | — | — | — | — | — | — | — | — | — |

Legend: ☐ = not started  ✓ = complete  — = not applicable

## Figures

Each chapter ends with a **Prompts** section containing ready-to-paste
prompts for recreating its D3 figures. Load `brutalist/CLAUDE.md` and
`brutalist/DESIGN.md` into your Claude project context before using them.

Cowork enrichment generates:
- `images/cancer-research-fig-NN.svg` — static SVG (→ PNG for EPUB)
- `d3/cancer-research-fig-NN.html` — interactive D3 HTML

Convert SVGs to PNG:
```bash
node SCRIPTS/svg-to-png.mjs
```

## Extraction Pass

To populate the extraction directories from authored chapter sections:

```
Run the Cowork extraction prompt against chapters/
```

Each extraction directory contains a README.md explaining what it holds,
what headings it matches, and how it connects to Medhavy.

## Build

```bash
npm install        # first time only
./build.sh
```

Output goes to `output/` (gitignored).
