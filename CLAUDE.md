# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A deployable static website for **Pixel Verse Studios**, a fictional indie 16-bit narrative game studio. Plain HTML + a **compiled Tailwind stylesheet** (Tailwind v3.4.17 standalone CLI — no Node, npm or package.json). The styling loop: edit classes in HTML/JS → run `scripts/build-css.sh` (or `scripts/build-css.sh --watch` while editing) → commit the regenerated `assets/css/tailwind.css`. **A new utility class used in markup does nothing until the CSS is rebuilt.** No test suite; the acceptance check for structural changes is `python3 scripts/check_site.py` (run from the repo root).

Layout:

- `index.html`, `games.html`, `heros-journey.html`, `studio-lore.html`: the four pages
- `assets/css/tailwind.css`: the minified compiled Tailwind output (commit the regenerated file; run `scripts/build-css.sh` after any class change)
- `assets/css/site.css`: the hand-written shared component CSS (loaded after `tailwind.css` so its rules win). Defines `.btn`, `.btn-primary`, `.btn-secondary`, `.btn-sm`, `.card`, `.badge`, `.nav-link` (+ active state), `.stage-tab`, `.field` / `.field-label`, `.pixelated`, and the lightbox styles (`.lightbox`, `.lightbox.open`, `.lightbox-close`, `.lightbox-figure`, `body.lightbox-open`, and the `img[data-lightbox]` zoom cursor)
- `tailwind.config.js` (root): the CommonJS Tailwind config (`darkMode: "class"` + the custom colors/spacing/fonts/radii). `assets/css/tailwind.input.css`: the three `@tailwind` directives that the CLI compiles from. `scripts/build-css.sh`: downloads the Tailwind v3.4.17 standalone CLI binary to `bin/` if missing (the repo has no Node/npm) and runs the build; `bin/` is gitignored
- `assets/js/site.js`: shared end-of-body script (mobile menu, newsletter form, and the click-to-enlarge lightbox driven by `img[data-lightbox]`)
- `assets/js/studio-lore.js`: contact form feedback
- `assets/img/`: local art. `logo.jpg` (studio logo), `studio-workshop.jpg`, `assets/img/team/` (`mariam.jpg`, `salah.jpg`, `sleem.jpg` — the team portraits), plus two per-game folders: `assets/img/crab-quest/` (logo, sprites, and `screens/` — real gameplay screenshots) and `assets/img/space-x/` (logo, ship, asteroid, planets, and `screens/` — real gameplay and game-over screenshots)
- `design/source-media/`: the **user's original screenshots and portraits** (`game-screens/crab-quests/`, `game-screens/space_x/`, `team/`). They are the source of truth for the game screenshots. The web copies under `assets/img/*/screens/` and `assets/img/team/` are resampled JPEGs of these — when a screenshot needs to change, re-derive it from `design/source-media/`. Gameplay screenshots are preferred over raw level backgrounds (the old `level-*-bg.jpg` / `space-background.jpg` art was removed for them).
- `assets/favicon-32.png`, `assets/apple-touch-icon.png`: favicons resampled (nearest-neighbour) from the logo render
- `design/screens/{home,games,heros-journey,studio-lore}.png`: reference renders of each page
- `design/neo-arcade-narrative/DESIGN.md`: the design system the pages implement
- `design/bauhaus/DESIGN.md`: an alternate light-theme system (yellow/red/blue on off-white). **No page uses it** — it is marked as unused at the top

## Game content is real — never invent it

Crab Quest and Space X are real, playable games (the sources live outside this repo). The site describes them accurately:

- **Crab Quest** (Ages 5-99): 6 chapters — Kitchen Escape, Beach Run, Sea Floor Dodging, Shrimp Help, Predator Chase, Home Sweet Home. Controls: ←/→ or A/D move, SPACE jump, R restart, ENTER back to level select.
- **Space X** (Ages 5-99): an educational space shooter. 3 hearts, +1 point per asteroid, level = 1 + score/30, spawn interval 60→20 frames; a fact about one of 9 solar-system bodies appears at game over. Controls: ←/→ steer, SPACE start/fire, P pause, R restart, F fullscreen.

Never replace this with invented features, fake stats/steam wishlists, or stage names like "Claw of Destiny". The game titles are exactly "Crab Quest" and "Space X".

## Rules (every page, always)

- Shared parts are referenced, not duplicated: compiled `<link rel="stylesheet" href="assets/css/tailwind.css" />` immediately before `<link rel="stylesheet" href="assets/css/site.css" />` (site.css must stay after it so component classes win); end-of-body `<script defer src="assets/js/site.js"></script>` plus the page's own script when it has one (studio-lore → `studio-lore.js`). No other inline `<script>`/`<style>`.
- Full width everywhere: `w-full` and `px-space-md lg:px-margin xl:px-16` on every section; no `max-w-7xl`.
- Header and footer are shared structure; the only per-page header change is which nav link carries `aria-current="page"` (in both desktop and mobile navs). Footer is byte-identical across pages.
- Index: hero + game cards; games: both games in full; heros-journey: the **Story Spine** page. `heros-journey.html` is a fully static page (no JS): two stacked sections, `id="crab-quest"` and `id="space-x"`, each intro (logo + title) followed by story beats that alternate image/text; crab has 7 beats (one per real chapter), space has 5 (title screen, launch, rising stakes, game over, the fact you learn every run). Screenshots are wrapped in `<button type="button" class="block w-full text-left">` with `data-lightbox` and the shared lightbox enlarges them site-wide; real game screenshots should never be cropped (`object-contain`, not `object-cover`).
- Nav uses `data-path` slugs (`home` → `index.html`, `games` → `games.html`, `heros-journey` → `heros-journey.html`, `studio-lore` → `studio-lore.html`, `community` → `#newsletter`, `play-demo` → `games.html`).
- Use the component classes from `site.css` instead of raw button/card styling. Colors/sizes come from the Tailwind tokens (`surface-container-*`, `on-surface`, `primary`, `secondary`, `tertiary`, `font-*`/`text-*`, `space-*`).
- No decorative monospace "terminal" labels, no fake status readouts, and no " // " breadcrumb separators in visible text. Small sprites scaled up get `pixelated`/`image-rendering: pixelated`; real photos and downscaled renders get `rounded`.
- Keep images local under `assets/img/`; never reintroduce `https://lh3.googleusercontent.com` `src`s.

## Previewing

Open a page directly, or serve the folder so relative links (and `assets/`) work:

```sh
python3 -m http.server 8000   # then open http://localhost:8000/index.html
```

Pages need network access for Google Fonts / Material Symbols; all `<img>`s and the Compiled CSS load from `assets/`. Compare your rendering against the sibling `design/screens/*.png`.

## Design system gotchas

- The **Tailwind config and the YAML frontmatter** in `design/neo-arcade-narrative/DESIGN.md` agree (e.g. `primary #d0bcff`, `secondary #4cd7f6`, `tertiary #4edea3`, `background #0f131c`). The DESIGN.md **prose** describes a different palette (`#8B5CF6` violet, `#06B6D4` cyan, `#10B981` green, `#090D16` void). Treat the config/frontmatter as the source of truth.
- The prose mandates `border-radius: 0` and 2px white borders everywhere. The config sets `DEFAULT` radius to `0.25rem`, and the pages rely on hard offset shadows (`shadow-[4px_4px_0_0_#000000]`, hover `-translate` + `6px` shadow, active `translate` + `shadow-none`) instead of borders. The component classes in `site.css` are already rounded-0 with the offset shadow.
- `site.css` loads after the compiled `tailwind.css`, so utility classes cannot override component padding — add a `.btn-sm`-style variant to `site.css` instead of fighting it with utilities.
- Fonts: Space Grotesk for headings, labels, and badges; Inter for body text. Loaded once per page via the single consolidated Google Fonts `<link>`.
- Pages are dark-only (`<html class="dark">`, `darkMode: "class"`).

## Checks

Run `python3 scripts/check_site.py` after any structural change. It verifies, per page: a unique `<title>` and meta description, a favicon link, exactly one Google Fonts link, resolveable local refs/anchors, correct `data-path` hrefs, exactly the page's own `aria-current` nav links, the mobile-menu toggle markers, `id="newsletter"`, references to all three shared assets (`assets/css/tailwind.css`, `assets/css/site.css`, `assets/js/site.js`), and — case-insensitively — that no `FORBIDDEN` substring sneaks back in. That list includes `tailwind-config` (so no `id="tailwind-config"`) and `max-w-7xl`. It also checks that `assets/css/tailwind.css` exists and is non-trivial, and that `assets/js/tailwind.config.js` is gone (the config lives at the root now). It also requires every file under `assets/img/` to be referenced somewhere in the pages or JS/CSS, the real Crab Quest chapter names and Space X planets to appear, `id="crab-quest"` / `id="space-x"` on games.html, no direct `googleusercontent` references or Stitch directories at the root, and — for the Story Spine redesign — that `assets/js/heros-journey.js` is gone, the five spine phrases and both section ids live in `heros-journey.html` (no `<svg>`, no `?game=`, no explorer component ids), every `<img>` pointing at `assets/img/*/screens/` carries `data-lightbox`, and `assets/js/site.js` implements the lightbox.