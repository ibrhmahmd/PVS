# Issues

## #1 — Turn Stitch export into a deployable static site `[refactor]`

**Status:** done

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
- Header nav is `hidden xl:flex` with no fallback → no navigation at all below 1280px.

**Decisions (user, 2026-09-24):**
- Stay on Tailwind Play CDN (no build step) for now.
- `Play Demo` → `games.html`; `Community` → footer newsletter anchor `#newsletter`.
- Archive Stitch sources under `design/`; keep Bauhaus there marked unused.
- Add a mobile menu (below `xl`) in this pass.

**Acceptance criteria:**
- [x] Root layout: `index.html`, `games.html`, `heros-journey.html`, `studio-lore.html`, `assets/img/`, `design/`
- [x] All nav/logo links resolve; correct `aria-current` + active classes per page
- [x] Every page has a unique `<title>` and meta description, plus favicon
- [x] All images served from `assets/img/`; zero `googleusercontent` references remain
- [x] Mobile menu toggle below `xl` with the same nav links
- [x] One consolidated Google Fonts `<link>` per page
- [x] Footer newsletter form handled without page reload (on all 4 pages)
- [x] Stitch sources archived under `design/` (Neo-Arcade DESIGN.md, Bauhaus DESIGN.md marked unused, `screen.png` references, logo/avatar renders)
- [x] Every page renders the same as its `screen.png` (no visual regressions)
- [x] CLAUDE.md updated for the new layout

## #2 — Simplify the site: cut clutter, full width, real game content, shared assets `[refactor]`

**Status:** done

**Goal:** A calmer, full-width site whose game content matches the two real games (`~/Desktop/AswanProjects/Crab-game`, `~/Desktop/AswanProjects/space-game`), with shared code in one place.

**Decisions (user, 2026-09-24):**
- Cut every audit candidate (A1–A12, B1–B10) **except** the per-game hero's journey (kept and rewritten from source) and the arc chart (kept, relabelled).
- Remove **all** decorative monospace "terminal" labels.
- Content spans the full width (no `max-w-7xl` cap); paragraphs keep a readable measure.
- Real facts only for games; real game art replaces AI game images.
- Titles: **Crab Quest** (matches the in-game logo) and **Space X**.
- Space X hero's journey = its real gameplay loop (the code has no story).
- Studio & Lore: remove invented stats and Project Dawn; team + origin story stay as editable placeholders.
- Single delegation pass covering content, layout and code cleanup (shared config/CSS/JS files, reusable component classes).
- Real media added by the user: Crab Quest + Space X screenshots and team portraits (Mariam, Salah, Sleem — names only). Originals archived in `design/source-media/`.
- Hero's Journey page redesign: Pixar **Story Spine** beats (Once upon a time / One day / Because of that / Until finally / And ever since then) mapped to real chapters; both games stacked (no switch); arc chart removed.
- Screenshots displayed large site-wide, click to open full-size overlay.

**Acceptance criteria:**
- [x] `python3 scripts/check_site.py` passes (extended for this issue)
- [x] Crab Quest: 6 chapters mapped to journey stages, real mechanics/win conditions, real level art
- [x] Space X: 6-stage gameplay-loop journey, real controls/mechanics, 9 planet facts, real art
- [x] No invented claims (Steam/Switch releases, playtimes, ratings, fictional characters in game copy)
- [x] Shared Tailwind config / CSS / JS live in `assets/`; no inline copies
- [x] Pages render correctly at 1920px and 390px; no JS errors
- [x] CLAUDE.md updated

## #3 — Compile Tailwind instead of the Play CDN `[performance]`

**Status:** done

`cdn.tailwindcss.com` compiles CSS in every visitor's browser (console warning "should not be used in production", render delay). Replace it with a one-time build that outputs a static `assets/css/tailwind.css` from `assets/js/tailwind.config.js`, keeping the site deployable as plain files.

**Decision (user, 2026-09-24):** Tailwind **standalone CLI** binary — no Node/npm in the repo.

**Acceptance:** no `cdn.tailwindcss.com` reference; pages render identically at 1920px/390px; build command documented in CLAUDE.md; `check_site.py` passes.

## #4 — Footer links point nowhere `[bug]`

**Status:** open — needs real URLs from the user

itch.io, Discord, YouTube, Terms and Privacy links are `href="#"` on all four pages. Replace with real URLs; remove any the studio doesn't have (Terms/Privacy likely removed unless pages are written).

**Needs from user:** itch.io, Discord, YouTube URLs — user will paste them; any not provided get removed.

## #5 — Downloadable builds + "Play" buttons for both games `[feature]`

**Status:** blocked — game builds happen on the user's Windows 11 laptop. Game-side work is tracked in each game repo: `~/Desktop/AswanProjects/Crab-game/ISSUES.md` #1 and `~/Desktop/AswanProjects/space-game/ISSUES.md` #1–#2. This site's part (Play/Download buttons linking to the itch.io pages) starts once those pages exist.

Both games are Pygame Zero desktop apps with no download anywhere. Package them (e.g. itch.io pages, or zipped builds), then add "Play / Download" buttons on Home and Games.

**Decisions (user, 2026-09-24):** host on **itch.io** (one page per game; user-side account steps via `$wizard`); package **both** a PyInstaller Windows .exe and a source zip. Packaging work happens in the game repos (`~/Desktop/AswanProjects/`), tracked there.

## #6 — Real studio content on Studio & Lore `[docs]`

**Status:** open — needs facts from the user

Placeholder copy remains: the origin story, the AI-generated studio photo (`assets/img/studio-workshop.jpg`), empty team roles for Mariam/Salah/Sleem, and "© 2024" in the footer.

**Needs from user:** the studio's real story (who, when, why), team roles, a real photo or keep the art, and the correct year.

## #7 — Make the site kid-simple `[refactor]`

**Status:** done — awaiting user review and commit

Goal: code a curious 12-year-old could read top to bottom.

**Decisions (user, 2026-10-08):**
- Drop the newsletter form, the contact form and the mobile menu button (listed under Limits in the README).
- Replace compiled Tailwind with one hand-written `assets/css/styles.css` using purpose names.
- Merge the scripts into one plain-function `site.js` (lightbox only); delete `studio-lore.js`.
- Trim `scripts/check_site.py` to plain loops.

**Done:**
- [x] `styles.css` replaces `tailwind.css`, `site.css`, `tailwind.input.css`, `tailwind.config.js`, `scripts/build-css.sh` and `bin/`
- [x] All four pages rewritten with purpose class names; forms and mobile menu removed; the `Community` nav link removed
- [x] README with a Limits section; `CLAUDE.md` and `AGENTS.md` rewritten
- [x] `check_site.py` passes
- [x] Restored `assets/img/space-x/asteroid.png` and `ship.png`, which the "markting updates" commit deleted by mistake (broken images on games and journey pages)

**Note:** issues #1 and #3 describe the old Play CDN / Tailwind setup and the removed mobile menu and newsletter; they are history.

## #8 — Describe Space X's new Journey to Jupiter `[docs]`

**Status:** open — waiting for the real art (space-game `ISSUES.md` #5)

Space X was redesigned (space-game issues #4 and #7). It is no longer an endless asteroid shooter. It is now "Journey to Jupiter", a science Mission to find out if Europa's hidden ocean could hold life: Title screen → 1 Launch pad (walk the Hero, collect the 4-item Checklist before the 30 s Countdown, blast off) → 2 Earth orbit (dodge space junk) → 3 Asteroid belt (shoot asteroids) → 4 Europa (ice chunks need two hits, then the Ship scans for the ocean) → Jupiter win screen, with a Fact card after each Level.

- [ ] Update the Space X text on `index.html`, `games.html`, `studio-lore.html` and `heros-journey.html` to describe the Journey.
- [ ] Controls: Left/Right or the on-screen arrows to walk or fly, Space to start and shoot (auto-fire in the belt and on Europa), P or the pause button to pause, R to retry, F for fullscreen.
- [ ] Replace screenshots once the final art lands (Launch pad, Ship and belt are still placeholders).
