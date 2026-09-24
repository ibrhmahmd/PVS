# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A Google Stitch export for **Pixel Verse Studios**, a fictional indie 16-bit narrative game studio. It holds static HTML mockups and design-system docs. There is no package manager, build step, linter, or test suite, and the directory is not a git repo.

Each Stitch "screen" is its own directory:

- `pixel_verse_studios_{home,games_portfolio,studio_lore,the_hero_s_journey}/`: a `code.html` page plus a `screen.png` reference render
- `pixel_verse_studios_logo/`, `charming_16_bit_pixel_art_avatar_…/`: image-only assets (`screen.png`, 1024×1024)
- `neo_arcade_narrative/DESIGN.md`: the design system the pages implement
- `bauhaus/DESIGN.md`: an alternate light-theme system (yellow/red/blue on off-white). **No page uses it.**

## Previewing

Open a page directly, or serve the folder so relative links work:

```sh
python3 -m http.server 8000   # then open http://localhost:8000/pixel_verse_studios_home/code.html
```

Pages need network access. Tailwind (Play CDN `cdn.tailwindcss.com`), Google Fonts, Material Symbols, and most images all load remotely. Compare your rendering against the sibling `screen.png`.

## Page architecture

Every `code.html` is fully self-contained, and the four pages duplicate their shared parts. A change to any of the following must be made in all four files:

- **Tailwind config**: the inline `<script id="tailwind-config">` in `<head>`, byte-identical across pages. It defines the Material-3-style color tokens (`surface-container-*`, `on-surface`, `primary`, `secondary`, `tertiary`, …), spacing tokens (`space-xs`…`space-xl`, `gutter`, `margin`), and paired `font-*`/`text-*` typography tokens (`display-hero`, `headline-*`, `body-*`, `label-code`, `label-badge`, plus `-mobile` variants). Use these tokens in markup rather than raw Tailwind colors or sizes.
- **Base `<style>` block**: scrollbar hiding, overscroll, and the `.scanline-overlay` CRT effect.
- **`<header>`**: identical except for the active nav item. The active link carries `aria-current="page"` plus `text-secondary bg-surface-container-high shadow-[2px_2px_0_0_#4cd7f6]` (also recorded in the nav's `data-active-classes`). Nav links use `data-path` slugs (`home`, `games`, `heros-journey`, `studio-lore`, `community`, `play-demo`), but every `href` is `#`: pages are not linked to each other, and the `community` and `play-demo` pages don't exist.
- **`<footer>`**: byte-identical across all four pages, including a newsletter `<form>` that has no handler.

Page-specific JS lives in one trailing inline `<script>` per page (vanilla, no dependencies):

- **home**: studio-reel modal (`#open-reel-btn` / `#reel-modal`) and quest signup form (`#quest-signup-form` → `#signup-confirmation`)
- **studio_lore**: contact form (`#transmission-form` → `#form-feedback`, resets after 4.5s) and `.team-card` click toggles
- **the_hero_s_journey**: the largest script. A `stagesData` object (stages 1–6) drives `#stage-btn-N` buttons that populate the `#card-stage-*` fields, plus the `#tab-crab` / `#tab-space` / `#tab-split` comparison tabs. Stage copy lives in JS, not in the markup.
- **games_portfolio**: no script

## Design system gotchas

- The **Tailwind config and the YAML frontmatter** in `neo_arcade_narrative/DESIGN.md` agree (e.g. `primary #d0bcff`, `secondary #4cd7f6`, `tertiary #4edea3`, `background #0f131c`). The DESIGN.md **prose** describes a different palette (`#8B5CF6` violet, `#06B6D4` cyan, `#10B981` green, `#090D16` void). Treat the config/frontmatter as the source of truth.
- The prose mandates `border-radius: 0` and 2px white borders everywhere. The config sets `DEFAULT` radius to `0.25rem`, and the pages mostly rely on hard offset shadows (`shadow-[4px_4px_0_0_#000000]`, with hover `-translate` + `6px` shadow and active `translate` + `shadow-none`) rather than borders.
- Fonts: Space Grotesk for headings, labels, and badges; Inter for body text. The pages load both, plus Material Symbols, twice via overlapping Google Fonts `<link>`s.
- Pages are dark-only (`<html class="dark">`, `darkMode: "class"`).

## Assets

Most `<img>` tags hotlink `lh3.googleusercontent.com/aida-public/...`. These are Stitch-generated, non-permanent URLs. Many images carry a `data-alt` attribute holding the generation prompt, which is useful for regenerating or replacing them. The only local images are the `screen.png` files.
