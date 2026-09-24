# Issues

## #1 — Turn Stitch export into a deployable static site `[refactor]`

**Status:** approved — delegated to OpenCode (`refactor` lane)

**Goal:** Plain HTML + Tailwind Play CDN site that can be dropped onto any static host (Netlify / GitHub Pages / Vercel) with working navigation and no dependency on expiring Stitch image URLs.

**Current problems (verified 2026-09-24):**
- Pages live at `<stitch_dir>/code.html`; no `index.html`.
- Every nav/logo `href` is `#`; pages are not linked to each other.
- `studio_lore` and `the_hero_s_journey` headers have no active nav item (`aria-current` missing).
- No `<title>` or meta description on any page.
- 24 unique images hotlinked from `lh3.googleusercontent.com/aida-public/…` (Stitch temp URLs; all 200 as of today).
- Google Fonts / Material Symbols requested twice per page via overlapping `<link>`s.
- Footer newsletter `<form>` (identical on all 4 pages) has no handler → full page reload on submit.
- Nav targets `community` and `play-demo` have no page.
- Unused `bauhaus/` design doc mixed in with site files.

**Decisions (user, 2026-09-24):**
- Stay on Tailwind Play CDN (no build step) for now.
- `Play Demo` → `games.html`; `Community` → footer newsletter anchor `#newsletter`.
- Archive Stitch sources under `design/`; keep Bauhaus there marked unused.

**Acceptance criteria:**
- [ ] Root layout: `index.html`, `games.html`, `heros-journey.html`, `studio-lore.html`, `assets/img/`, `design/`
- [ ] All nav/logo links resolve; correct `aria-current` + active classes per page
- [ ] Every page has a unique `<title>` and meta description, plus favicon
- [ ] All images served from `assets/img/`; zero `googleusercontent` references remain
- [ ] One consolidated Google Fonts `<link>` per page
- [ ] Footer newsletter form handled without page reload (on all 4 pages)
- [ ] Stitch sources archived under `design/` (Neo-Arcade DESIGN.md, Bauhaus DESIGN.md marked unused, `screen.png` references, logo/avatar renders)
- [ ] Every page renders the same as its `screen.png` (no visual regressions)
- [ ] CLAUDE.md updated for the new layout
