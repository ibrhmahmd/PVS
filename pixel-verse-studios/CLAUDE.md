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

- **Crab Quest** (Ages 5-99): 6 chapters — Kitchen Escape, Beach Run, Sea Floor Dodging, Shrimp Help, Predator Chase, Home Sweet Home. Controls: ←/→ or A/D move, SPACE jump, R restart, ENTER back to level select, ESC leaves a chapter (back to the chapter select).
- **Space X: Journey to Jupiter** (Ages 5-99): the Hero's Mission is to fly to Europa, Jupiter's icy moon, and find out if its hidden ocean could hold life. Title screen → Level 1 Launch pad (walk the Hero, collect the 4-item Checklist: helmet, ammo crate, lucky football, fuel can; board the Ship before the 30 s Countdown ends) → Level 2 Earth orbit (dodge 10 pieces of space junk, no shooting) → Level 3 Asteroid belt (shoot 30 asteroids; auto-fire every half second, SPACE adds shots, faster as you score) → Level 4 Europa (12 ice chunks, two hits each, then a 3 s scan: "Ocean found!") → Jupiter win screen (score + high score, R flies again). A Fact card after every Level. The 3 flying Levels give 3 hearts; losing them all (or the Countdown) shows a random fact about the Sun or one of the 8 planets, and R retries the same Level. Moon facts: Jupiter has more than 100 moons, Saturn more than 280. Controls: ←/→ or the on-screen LEFT/RIGHT buttons walk or fly, SPACE start/continue/shoot, P or the pause button pause, R retry / fly again, F fullscreen.
- Titles are exactly "Crab Quest" and "Space X" ("Journey to Jupiter" is Space X's subtitle, used in text, not headings). No fake stats, wishlists or invented stage names.

## Rules for every page

- Head: one Google Fonts `<link>`, then `assets/css/styles.css`. End of body: `<script defer src="assets/js/site.js">`. No inline `<script>` or `<style>`.
- Nav links use `data-path` slugs (`home`, `games`, `heros-journey`, `studio-lore`, `play-demo` → `games.html`).
- `heros-journey.html` is the **Story Spine** page: sections `id="crab-quest"` (7 beats) and `id="space-x"` (6 beats), each beat a picture next to its story, alternating sides (`.beat` / `.beat-flip`).
- Screenshots are `<img data-lightbox="caption">` inside `<button class="shot-button">`. Never crop real screenshots (`object-contain`, not `object-cover`, except the small card thumbnails on the home page). Small sprites get `.pixelated`.
- Keep images local under `assets/img/`. Every file there must be used by a page (the check enforces it).
- No decorative monospace "terminal" labels, no fake status readouts, no ` // ` separators in visible text.
