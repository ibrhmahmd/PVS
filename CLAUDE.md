# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A deployable static website for **Pixel Verse Studios**, a fictional indie 16-bit narrative game studio. Plain HTML + the Tailwind Play CDN — no package manager, no build step, no test suite, no external dependencies beyond the CDNs. The acceptance check for structural changes is `python3 scripts/check_site.py` (run from the repo root).

Layout:

- `index.html`, `games.html`, `heros-journey.html`, `studio-lore.html`: the four pages (moved from the Stitch `pixel_verse_studios_*/code.html` screens)
- `assets/img/*.jpg`: local copies of the images that used to be hotlinked from `lh3.googleusercontent.com`; `assets/favicon-32.png` and `assets/apple-touch-icon.png`: favicons resampled (nearest-neighbour) from the logo render
- `assets/img/` file names match the original image's `alt`/`data-alt`/context (e.g. `logo.jpg`, `profile-avatar.jpg`, `crab-quest-eel-boss.jpg`)
- `design/screens/{home,games,heros-journey,studio-lore}.png`: reference renders of each page
- `design/renders/logo.png`, `design/renders/dev-avatar.png`: the 1024×1024 Stitch image-only assets (logo is the favicon source)
- `design/neo-arcade-narrative/DESIGN.md`: the design system the pages implement
- `design/bauhaus/DESIGN.md`: an alternate light-theme system (yellow/red/blue on off-white). **No page uses it** — it is marked as unused at the top.

## Previewing

Open a page directly, or serve the folder so relative links (and `assets/`) work:

```sh
python3 -m http.server 8000   # then open http://localhost:8000/index.html
```

Pages need network access. Tailwind (Play CDN `cdn.tailwindcss.com`) and Google Fonts / Material Symbols load remotely; all `<img>`s load from `assets/img/`. Compare your rendering against the sibling `design/screens/*.png`.

## Page architecture

The four pages duplicate their shared parts. A change to any of the following must be made in all four files:

- **Tailwind config**: the inline `<script id="tailwind-config">` in `<head>`, byte-identical across pages. It defines the Material-3-style color tokens (`surface-container-*`, `on-surface`, `primary`, `secondary`, `tertiary`, …), spacing tokens (`space-xs`…`space-xl`, `gutter`, `margin`), and paired `font-*`/`text-*` typography tokens (`display-hero`, `headline-*`, `body-*`, `label-code`, `label-badge`, plus `-mobile` variants). Use these tokens in markup rather than raw Tailwind colors or sizes.
- **Base `<style>` block**: scrollbar hiding, overscroll, and the `.scanline-overlay` CRT effect. Its contents must stay byte-identical across pages.
- **`<head>`**: each page has its own `<title>` and meta description, plus the same `theme-color`, `favicon-32.png` / `apple-touch-icon.png` links, and exactly ONE Google Fonts stylesheet `<link>` (both preconnects and the fonts URL are identical across pages).
- **`<header>`**: identical except for the per-page active nav item. The active link carries `aria-current="page"` plus `text-secondary bg-surface-container-high shadow-[2px_2px_0_0_#4cd7f6]` on the shared active class list (also recorded in the nav's `data-active-classes`). Nav links use `data-path` slugs (`home`, `games`, `heros-journey`, `studio-lore`, `community`, `play-demo`) and resolve to real hrefs: `index.html`, `games.html`, `heros-journey.html`, `studio-lore.html`, `#newsletter`, `games.html`. `community` and `play-demo` pages don't exist; `community` targets the footer newsletter anchor. Below the `xl` breakpoint the desktop nav (`hidden xl:flex`) is replaced by a mobile menu button (`#mobile-menu-btn`, `xl:hidden`) and a stacked panel `#mobile-nav` with the same five links.
- **`<footer>`**: byte-identical across all four pages. Contains the newsletter column `#newsletter` with `<form id="newsletter-form">` (input `name="email"`, button `type="submit"`), a hidden `#newsletter-confirmation`, and a Press Kit link to `studio-lore.html#press-inquiries` (the only footer link with a real destination — Steam/itch.io/Discord/YouTube/Terms/Privacy stay `href="#"`).
- **Shared end-of-body `<script>`**: byte-identical across all four pages, right before `</body>`, separate from the page-specific script. It toggles the mobile menu (switch `menu`/`close` icon, `aria-expanded`, closes on Escape and on link click) and handles the newsletter submit (preventDefault, hide the form, show the confirmation).

Page-specific JS lives in one trailing inline `<script>` per page (vanilla, no dependencies); do not edit them:

- **home (index.html)**: studio-reel modal (`#open-reel-btn` / `#reel-modal`) and quest signup form (`#quest-signup-form` → `#signup-confirmation`)
- **studio-lore**: contact form (`#transmission-form` → `#form-feedback`, resets after 4.5s) and `.team-card` click toggles
- **heros-journey**: the largest script. A `stagesData` object (stages 1–6) drives `#stage-btn-N` buttons that populate the `#card-stage-*` fields, plus the `#tab-crab` / `#tab-space` / `#tab-split` comparison tabs. Stage copy lives in JS, not in the markup.
- **games**: no script

## Design system gotchas

- The **Tailwind config and the YAML frontmatter** in `design/neo-arcade-narrative/DESIGN.md` agree (e.g. `primary #d0bcff`, `secondary #4cd7f6`, `tertiary #4edea3`, `background #0f131c`). The DESIGN.md **prose** describes a different palette (`#8B5CF6` violet, `#06B6D4` cyan, `#10B981` green, `#090D16` void). Treat the config/frontmatter as the source of truth.
- The prose mandates `border-radius: 0` and 2px white borders everywhere. The config sets `DEFAULT` radius to `0.25rem`, and the pages mostly rely on hard offset shadows (`shadow-[4px_4px_0_0_#000000]`, with hover `-translate` + `6px` shadow and active `translate` + `shadow-none`) rather than borders.
- Fonts: Space Grotesk for headings, labels, and badges; Inter for body text. Loaded once per page via the single consolidated Google Fonts `<link>`.
- Pages are dark-only (`<html class="dark">`, `darkMode: "class"`).

## Checks

Run `python3 scripts/check_site.py` after any structural change — it verifies, per page: a unique `<title>` and meta description, a favicon link, exactly one Google Fonts link, resolveable local refs/anchors, correct `data-path` hrefs, exactly one (pair of) `aria-current` active nav links with the right classes, the mobile-menu toggle markers, and `id="newsletter"`. It also requires `assets/img/` to be populated and no direct `googleusercontent` references or Stitch directories at the root. Keep images local: never reintroduce `https://lh3.googleusercontent.com` `src`s.