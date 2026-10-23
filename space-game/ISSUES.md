# Issues

## #1 — Asset paths break when started from another folder `[bug]`

**Status:** fixed (`Game.py` changes into its own folder, or `sys._MEIPASS` when frozen, *before* `import pgzrun`, which overwrites `__file__`); still to confirm in a PyInstaller build

`Game.py` loaded files with cwd-relative paths: `pygame.image.load(current_planet_info["image"])` (paths like `images/Sun.png` from `game_data.py`) and `pygame.mixer.Sound('music/crash.mp3')`. Running the game from any other directory — or from a PyInstaller build — fails to find them. Resolve paths against the game's own folder (and `sys._MEIPASS` when frozen).

## #2 — Package Space X for players `[feature]`

**Status:** in progress — the Windows build runs on GitHub Actions (`.github/workflows/build-games.yml`); a Linux test build of the same command starts fine, which also confirms #1

- [ ] Windows build with PyInstaller on GitHub Actions (bundles `images/`, `music/`, `fonts/` with `fonts/OFL.txt`, and Pygame Zero's own data); download the `Space-X-windows` artifact
- [ ] Source zip with run instructions: install Python + `pip install pgzero`, then `python Game.py`
- [ ] itch.io page with screenshots, description, controls, both downloads
- [ ] Smoke-test the .exe on Windows (start, shoot, game over + planet fact, restart, pause, fullscreen toggle)

The Pixel Verse Studios website (issue #5) links its "Play" buttons to the itch.io page.

## #3 — Typo in the Jupiter fact `[bug]`

**Status:** fixed

`game_data.py` Jupiter text reads "Great Red Spot, a giant s-torm." — should be "storm".

## #4 — Earth-to-Jupiter Journey redesign `[feature]`

**Status:** implemented, uncommitted, awaiting review/playtest (headless full-flow test passes)

Replace the endless shooter with a Journey: Intro → Level 1 Earth → Level 2 Asteroid belt → Level 3 Europa → Jupiter win screen. Terms are defined in `CONTEXT.md`.

- [ ] **Intro**: original space background, Hero boards the Ship, Space launches Level 1.
- [ ] **Earth**: dodge space junk, Ship cannot shoot. **Belt**: shoot asteroids (only Level with asteroids). **Europa**: shoot ice chunks that take 2 hits (first hit swaps to a cracked sprite).
- [ ] Each Level ends at a points target (one number per Level in `data/level_data.py`), then shows a Fact card.
- [ ] Game over: random planet fact (`data/game_data.py`), R retries the same Level with 3 hearts. High score stays in memory.
- [ ] Win screen on Jupiter background: Hero, Jupiter fact, score + high score, R flies again from Earth.
- [ ] Story (Mission): the Hero flies to check whether Europa's ocean could hold life. Story lines on the Intro, each Fact card and the win screen (`data/level_data.py`); Europa's ice comes from its water plumes.
- [ ] Controls: keyboard (arrows, Space, P, R, F) + clickable left/right/pause/continue buttons; Ship auto-fires in shooting Levels.
- [ ] Kid-simple code: `Game.py` has only the Pygame Zero hooks and switches on `game_mode`; code organised into `screens/`, `levels/`, `parts/`, `data/`; no try/except; assets resolved from the game folder (also fixes #1).

## #5 — Prepare new art for use `[feature]`

**Status:** in progress. Generated with Antigravity 2026-10-08 and wired in: Earth orbit, Jupiter and Title backgrounds, junk, ice + cracked ice (stray pixel and magenta tint cleaned). Belt background had rocks that looked like the real asteroids: dimmed for now, prompt #3 rewritten for a version without rocks. Pixel font Jersey 10 (OFL) with a black outline on all text. Launch pad background and planet pictures added 2026-10-15. Football added 2026-10-15; current Ship, heart and dimmed Belt background accepted as final. Still to make: 4 Checklist items. Prompts and a status table are in `docs/art-prompts.md`

- [ ] `characters/hero.png` and `sprites/asteroid.png`: remove white background, shrink (hero ~150px tall, asteroid ~120px), keep originals in `images/originals/`.
- [ ] `buttons/*.jpeg` → PNG with transparent corners.
- [ ] Crop/resize `backgrounds/uropa.png` (typo for "europa", rename) to 800×600.
- [ ] Still to design (placeholders until then): Earth, belt and Jupiter backgrounds; space-junk and ice-chunk (and cracked) sprites; football bullet; pixel heart; ship matching the Hero style.

## #6 — Hero art shows real-world logos `[bug]`

**Status:** open — release blocker for #2

`characters/hero.png` shows the Puma mark and the Egypt FA badge. Kept deliberately for now. Replace or remove before the public itch.io release.

## #7 — Launch pad Level, Title screen and Europa Scan `[feature]`

**Status:** implemented on branch `journey-fixes`, uncommitted; real-loop smoke test passes; awaiting your playtest and review

Design agreed 2026-10-08. Terms are in `CONTEXT.md`.

- [ ] **Title screen** replaces the Intro: original space background, logo, Hero, Mission, high score, "Press Space to start". No boarding scene.
- [ ] **Level 1 Launch pad**: side view, walk the Hero left/right (faces the way he walks, no jump). 30 s Countdown. 4 Checklist items (helmet, ammo crate, lucky football, fuel can) at random spots, one per zone (one zone behind the start). 1 point per item. HUD: Countdown + item icons, no hearts. Door stays shut until all 4 are collected; then the Hero boards and the Ship blasts off. Countdown at 0 = game over, R retries with new spots.
- [ ] Levels renumbered: 2 Earth orbit (dodge junk), 3 Asteroid belt, 4 Europa.
- [ ] **Europa Scan**: after the points target, ice stops, a 3 s automatic Scan, then "Ocean found!" and the Fact card.
- [ ] Each Level decides when it is cleared (`game_states.level_cleared`), instead of `Game.py` checking the points target.
- [ ] Placeholder art: Launch pad background, 4 item icons, small Hero (and mirrored), Ship on the pad. Real art prompts in `docs/art-prompts.md`.

## #8 — Gameplay fixes before packaging `[bug]`

**Status:** fixed (verified by a headless play-through)

Found by a headless play-through audit (2026-10-15).

- [x] Launch pad Countdown is 5 s (`COUNTDOWN_SECONDS = 5`, a leftover test value); #7 says 30 s.
- [x] Long game-over facts (Sun, Mercury, Venus) run under the "GAME OVER" title. Make every fact fit above it.
- [x] A click or Space right after dying or clearing a Level skips the game-over fact or Fact card at once. Ignore input for the first second on those screens.
- [x] Moon counts are out of date (Jupiter 79, Saturn 82, Uranus 27, Neptune 14). Mid-2026 counts: Jupiter about 101, Saturn 285, Uranus 28-29, Neptune 16.

Left as is: F (fullscreen) raises an error under a dummy video driver but works on real displays (kid-simple rules forbid try/except); unpausing restarts the music; the Ship overlaps the move buttons by 10 px.
