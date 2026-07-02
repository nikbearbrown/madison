<!-- repo: https://github.com/nikbearbrown/quantum-mechanics-videos | stars: 1 | updated: 2026-06-25T21:07:08Z -->

# Medhavy's Notes — Quantum Mechanics Videos

Source + tooling for the **Medhavy's Notes** quantum-mechanics video series on
[youtube.com/@MedhavyAI](https://www.youtube.com/@MedhavyAI). Narrated explainers and
scientist mini-bios, built with Manim + ElevenLabs.

You (the fellows) author, render a **16:9**, get it **approved by Sri**, and only then
publish + cut the **9:16** Short. This README is your getting-started; `HANDOFF.md` is the
command reference.

---

## Getting started

### 1. Pick your books
There are five quantum-mechanics volumes (`quantum-mechanics-vol1` … `vol5`). **Each fellow
takes two — and no two fellows share a book.** Before you start, claim your two in
`BOOKS.md` (name → the two volumes) so coverage doesn't collide. Work only your books.

### 2. Set up (once)
- macOS with the `ai` Python env (Manim Community, `mutagen`, `requests`), **MacTeX** (math),
  and **ffmpeg**.
- **ElevenLabs key** (sent to you separately) — in your shell, never in a file:
  ```
  export ELEVENLABS_API_KEY="the-key-you-were-given"      # add to ~/.zshrc
  ```
  Never paste the key into a script, beat sheet, or commit. It is never stored in this repo.
- **Fonts** — install both families locally and drop their `.ttf` into each video's `fonts/`:
  - [Montserrat](https://fonts.google.com/specimen/Montserrat) (display/UI — already shipped in `tools/templates/fonts/`)
  - [Architects Daughter](https://fonts.google.com/specimen/Architects+Daughter) (handwritten — **download and add**)
- **Voice** — Medhavy is `1sgY6Voq1aexKOB1IJ2D`, already the default in the tooling.

### 3. Make a 16:9 video
Run everything **from the video's folder**; scripts live at `../tools/scripts/`.

Mini-bio (scientist):
```
python ../tools/scripts/new_bio.py "Niels Bohr"     # scaffolds bio-niels-bohr/
# edit beat_sheet.json (narration + cards + clip prompts)
python ../tools/scripts/generate_audio.py .         # Medhavy VO (needs the env key)
manim -qh bio_niels_bohr.py BearsDoodlesVideo
# generate the clip prompts in Higgsfield → drop mp4s in TMP/ named B1_, B3_, B5_, B7_
python ../tools/scripts/ingest_clips.py .
python ../tools/scripts/composite_clips.py .
python ../tools/scripts/assemble.py . --mode manim --manim-mp4 mp4/_composited.mp4
python ../tools/scripts/package_bio.py .            # drafts the YouTube title/description
```
Concept explainer: open the concept folder, set `metadata.voice_id` to the Medhavy voice,
then `generate_audio.py .` → `manim -qh <scene>.py BearsDoodlesVideo` → `assemble.py . --mode manim`.
(Re-render audio **and** video so it's fully Medhavy.)

### 4. Self-check (before Sri sees it)
```
python ../tools/scripts/manim_layout_audit.py <scene>.py     # exit 0 = clean
```
Then watch the 16:9 and confirm: text never overlaps or leaves frame; the picture fills the
frame; **the voice matches what's on screen**; **no leftover FOOTAGE placeholder**; the
**name, dates, and equation are correct**; clean final frame.

### 5. Approval loop
1. **Render the 16:9.** Self-check it (step 4).
2. **Upload it UNLISTED** to YouTube and **send the link to Sri.**
3. **If Sri approves** → set the video **Public**, *then* cut the **9:16 Short** and publish it:
   ```
   manim -r 1080,1920 --fps 60 --disable_caching --flush_cache <scene>.py BearsDoodlesVideo
   python ../tools/scripts/composite_clips.py . --portrait
   python ../tools/scripts/assemble.py . --mode manim --portrait --manim-mp4 mp4/_composited-short.mp4
   ```
4. **If Sri leaves notes** → paste his notes, fix the beat sheet / scene, **re-render**, upload
   a new unlisted version, and **send again.** Repeat until approved.

Nothing goes Public, and no 9:16 is made, before Sri approves the 16:9.

---

## Brand — Medhavy's Notes
Defined in [`tools/brands/medhavy.json`](tools/brands/medhavy.json).

**Fonts**
- **Montserrat** — display / titles / UI.
- **Architects Daughter** — handwritten / whiteboard text.
- **LaTeX** (Manim `MathTex`) — *all* math. Never set equations in a text font.

**Color — the Okabe-Ito palette** (colorblind-safe; endorsed by *Nature Methods*; readable
under deuteranopia, protanopia, tritanopia). Use it for any color-coded/categorical element;
don't invent off-palette colors.

| name | hex |
|------|-----|
| black | `#000000` |
| orange | `#E69F00` |
| sky blue | `#56B4E9` |
| bluish green | `#009E73` |
| yellow | `#F0E442` |
| blue | `#0072B2` |
| vermillion | `#D55E00` |
| reddish purple | `#CC79A7` |

Two visual styles share these tokens: **cinematic-dark** (mini-bios: white on near-black) and
**whiteboard** (explainers: Architects Daughter on white). See the brand file for both.

---

## Layout
```
tools/scripts/     pipeline (generate_audio, manim_layout_audit, composite_clips, assemble,
                   ingest_clips, new_bio, package_bio, …)
tools/templates/   bio scene + fonts + bn_layout (for new_bio)
tools/skills/      authoring guides (whiteboard, mini-bio, scout)
tools/brands/      medhavy.json · whiteboard.json
BOOKS.md           who's working which two volumes
<slug>/            one folder per video: beat_sheet.json, <scene>.py, fonts/, mp4/<master>
```

## Keys & git safety
**No API keys live in this repo.** The ElevenLabs key is read from `ELEVENLABS_API_KEY`;
YouTube OAuth files stay local. `.gitignore` already blocks `*.env`, `client_secret*.json`,
`token*.json`, `*secret*`, `*.key`, `media/`, `mp3/`, `clips/`, `TMP/`. Before any commit:
```
git status
git diff --cached --name-only | grep -iE "secret|token|\.env|\.key" && echo "STOP" || echo "clean"
```
**Source-only repo:** committed = beat sheets, scenes, fonts, scripts, brand, docs. Not
committed = anything rendered (`mp4/`, `mp3/`, `clips/`, `media/`) — all of it is regenerated
locally from source (audio = ElevenLabs, video = Manim, footage = Higgsfield). Full detail and
the first-push steps are in **HANDOFF.md**.
