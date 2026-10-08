# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A deployable static website for **Pixel Verse Studios**, a fictional indie 16-bit narrative game studio. Four plain HTML pages, one hand-written stylesheet, one small script. No Node, npm, Tailwind or build step. Open the pages directly or run `python3 -m http.server 8000`.

The only check is `python3 scripts/check_site.py` (run from the repo root). Run it after any structural change.

## Kid-simple rules (keep them)

This project was refactored to be **kid-simple**: code a curious 12-year-old could read top to bottom and explain back. Keep it that way.

- Plain code: plain variables and functions with verb names (`open_lightbox`), loops and `if`s, no IIFEs, classes, arrow functions or clever one-liners. One short kid-word comment above anything a kid would ask "why?" about.
- No new library or tool unless it does a job that plain code cannot do in about 10 lines. The site uses only Google Fonts and Material Symbols, loaded by one `<link>`.
- CSS: class names say what a thing IS (`.card`, `.badge`, `.beat`), not how it looks. Colours and sizes are variables at the top of `assets/css/styles.css`. Do not add utility-class frameworks.
- Repetition beats abstraction: the header and footer are copied into each page on purpose (the only difference is which nav link has `aria-current="page"`).
- Every simplification that removes a feature or safety goes in the README's **Limits** section. Removed on purpose: newsletter form, contact form, mobile menu button.

## Layout

- `index.html`, `games.html`, `heros-journey.html`, `studio-lore.html`
- `assets/css/styles.css`: all styles, numbered sections (colours, basics, grids, header, text, buttons/cards, story beats, pictures, footer, lightbox, side gaps last)
- `assets/js/site.js`: the click-to-enlarge lightbox, driven by `img[data-lightbox]`
- `assets/img/`: local art. `crab-quest/` and `space-x/` hold logos, sprites and `screens/` (real gameplay screenshots); `team/` the portraits
- `design/source-media/`: the user's original screenshots and portraits. Web copies are resampled JPEGs of these; re-derive from the originals when a screenshot changes
- `design/neo-arcade-narrative/DESIGN.md`: the design system. Its YAML frontmatter colours (`#d0bcff`, `#4cd7f6`, `#4edea3`, `#0f131c`) are the source of truth, not its prose palette. `design/bauhaus/` is unused
- `scripts/check_site.py`: the acceptance check

## Game content is real — never invent it

- **Crab Quest** (Ages 5-99): 6 chapters — Kitchen Escape, Beach Run, Sea Floor Dodging, Shrimp Help, Predator Chase, Home Sweet Home. Controls: ←/→ or A/D move, SPACE jump, R restart, ENTER back to level select.
- **Space X** (Ages 5-99): educational space shooter. 3 hearts, +1 point per asteroid, level = 1 + score/30, spawn interval 60→20 frames; a fact about one of 9 solar-system bodies at game over. Controls: ←/→ steer, SPACE start/fire, P pause, R restart, F fullscreen.
- Titles are exactly "Crab Quest" and "Space X". No fake stats, wishlists or invented stage names.

## Rules for every page

- Head: one Google Fonts `<link>`, then `assets/css/styles.css`. End of body: `<script defer src="assets/js/site.js">`. No inline `<script>` or `<style>`.
- Nav links use `data-path` slugs (`home`, `games`, `heros-journey`, `studio-lore`, `play-demo` → `games.html`).
- `heros-journey.html` is the **Story Spine** page: sections `id="crab-quest"` (7 beats) and `id="space-x"` (5 beats), each beat a picture next to its story, alternating sides (`.beat` / `.beat-flip`).
- Screenshots are `<img data-lightbox="caption">` inside `<button class="shot-button">`. Never crop real screenshots (`object-contain`, not `object-cover`, except the small card thumbnails on the home page). Small sprites get `.pixelated`.
- Keep images local under `assets/img/`. Every file there must be used by a page (the check enforces it).
- No decorative monospace "terminal" labels, no fake status readouts, no ` // ` separators in visible text.
