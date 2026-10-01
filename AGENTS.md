# AGENTS.md — Pixel Verse Studios

Static site for an indie game studio. Plain HTML + compiled Tailwind (v3.4.17 standalone CLI — no Node/npm).

## Critical workflow

**Styling loop:** Edit classes in HTML/JS → `scripts/build-css.sh` → commit regenerated `assets/css/tailwind.css`.  
New utility classes do nothing until CSS is rebuilt. Watch mode: `scripts/build-css.sh --watch`.

**Verify after structural changes:**
```bash
python3 scripts/check_site.py
```
Runs from repo root. Checks: unique titles/meta, favicon, 1 Google Fonts link, valid local refs/anchors, correct `data-path` hrefs, correct `aria-current` nav links, mobile menu markers, `id="newsletter"`, all 3 shared assets linked, no forbidden strings, no inline `<style>`/`<script>`, real game content present, all images referenced, Tailwind CSS exists and is non-trivial, no leftover Stitch dirs.

## Key commands

| Task | Command |
|------|---------|
| Build CSS | `scripts/build-css.sh` |
| Watch CSS | `scripts/build-css.sh --watch` |
| Verify site | `python3 scripts/check_site.py` |
| Preview locally | `python3 -m http.server 8000` |

## Architecture facts

- **4 pages:** `index.html`, `games.html`, `heros-journey.html`, `studio-lore.html`
- **Shared assets (load order matters):**
  1. `<link rel="stylesheet" href="assets/css/tailwind.css" />`
  2. `<link rel="stylesheet" href="assets/css/site.css" />` (wins on component classes)
  3. `<script defer src="assets/js/site.js"></script>` + page-specific script (only `studio-lore.js`)
- **No inline `<style>` or `<script>`** — check_site.py fails on these
- **Full width everywhere:** `w-full px-space-md lg:px-margin xl:px-16` on every section; **no `max-w-7xl`**
- **Header/footer shared** — only `aria-current="page"` differs per page (desktop + mobile navs)
- **Dark mode only:** `<html class="dark">`, `darkMode: "class"`

## Game content — never invent

- **Crab Quest** (Ages 5-99): 6 chapters — Kitchen Escape, Beach Run, Sea Floor Dodging, Shrimp Help, Predator Chase, Home Sweet Home
- **Space X** (Ages 5-99): educational shooter, 3 hearts, +1/asteroid, level = 1 + score/30, spawn 60→20 frames, 9 solar-system facts at game over
- Titles are exactly "Crab Quest" and "Space X" — no fake stats, Steam wishlists, or invented stage names

## Design system gotchas

- **Source of truth:** Tailwind config + DESIGN.md YAML frontmatter (e.g. `primary #d0bcff`, `secondary #4cd7f6`, `tertiary #4edea3`, `background #0f131c`). DESIGN.md prose describes a different palette — ignore it.
- **No borders:** Pages use offset shadows (`shadow-[4px_4px_0_0_#000000]`, hover `-translate` + `6px`, active `translate` + `shadow-none`). Component classes in `site.css` are `border-radius: 0` with offset shadows.
- **`site.css` loads after `tailwind.css`** — utilities can't override component padding. Add variants (`.btn-sm`) to `site.css` instead.
- **Fonts:** Space Grotesk (headings/labels/badges), Inter (body). One consolidated Google Fonts `<link>` per page.
- **Small sprites** → `.pixelated` / `image-rendering: pixelated`. Real photos/downscaled → `rounded`.

## Image handling

- **Source of truth:** `design/source-media/` (original screenshots/portraits)
- **Web copies:** `assets/img/*/screens/` and `assets/img/team/` are resampled JPEGs. Re-derive from source when changing.
- **Gameplay screenshots preferred** over raw level backgrounds.
- **Never crop real screenshots:** use `object-contain`, not `object-cover`.
- **Lightbox:** wrap screenshots in `<button type="button" class="block w-full text-left">` with `data-lightbox`; `site.js` handles enlargement site-wide.
- **All images local** under `assets/img/` — no `googleusercontent.com` sources.

## Nav structure

`data-path` slugs:
- `home` → `index.html`
- `games` → `games.html`
- `heros-journey` → `heros-journey.html`
- `studio-lore` → `studio-lore.html`
- `community` → `#newsletter`
- `play-demo` → `games.html`

## Component classes (from `site.css`)

`.btn`, `.btn-primary`, `.btn-secondary`, `.btn-sm`, `.card`, `.badge`, `.nav-link` (+ `[aria-current="page"]`), `.stage-tab`, `.field`/`.field-label`, `.pixelated`, lightbox styles (`.lightbox`, `.lightbox.open`, `.lightbox-close`, `.lightbox-figure`, `body.lightbox-open`, `img[data-lightbox]`).

## Forbidden patterns (checked by check_site.py)

- Invented names: `barnaby`, `jax thalas`, `project dawn`, `beyond the nebula`, `claw of destiny`, `steamworks`, `steam deck`, `wishlist`, `nintendo`, `4.9 / 5`, `500k`, `420k`, `98.4`, `8-bit on`, `scanline`
- Removed components: `reel-modal`, `elena rostova`, `sys.ready`, `crab game`, `comparison-container`, `quest-signup-form`, `elena vance`, `kai chen`, `mira soren`, `leo marchetti`, `both are free`, `four people`
- Structural: `max-w-7xl`, `tailwind-config`, `cdn.tailwindcss.com`, `assets/js/tailwind.config.js`
- Decorative ` // ` labels in visible text