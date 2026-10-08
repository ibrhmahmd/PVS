# Issues

## #1 — Asset paths break when started from another folder `[bug]`

**Status:** fixed in the Journey redesign (`Game.py` changes into its own folder, or `sys._MEIPASS` when frozen); still to confirm in a PyInstaller build

`Game.py` loaded files with cwd-relative paths: `pygame.image.load(current_planet_info["image"])` (paths like `images/Sun.png` from `game_data.py`) and `pygame.mixer.Sound('music/crash.mp3')`. Running the game from any other directory — or from a PyInstaller build — fails to find them. Resolve paths against the game's own folder (and `sys._MEIPASS` when frozen).

## #2 — Package Space X for players `[feature]`

**Status:** open — blocked by #1; waiting for the Windows 11 build session

- [ ] Windows build with PyInstaller (bundle `images/` and `music/`)
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
- [ ] Controls: keyboard (arrows, Space, P, R, F) + clickable left/right/pause/continue buttons; Ship auto-fires in shooting Levels.
- [ ] Kid-simple code: `Game.py` has only the Pygame Zero hooks and switches on `game_mode`; code organised into `screens/`, `levels/`, `parts/`, `data/`; no try/except; assets resolved from the game folder (also fixes #1).

## #5 — Prepare new art for use `[feature]`

**Status:** cutouts, PNG buttons, `europa.png` and placeholders done; real Earth/belt/Jupiter backgrounds and junk/ice/football/heart/ship art still to design. Ready-to-paste prompts are in `docs/art-prompts.md`

- [ ] `characters/hero.png` and `asteroid.png`: remove white background, shrink (hero ~150px tall, asteroid ~120px), keep originals in `images/originals/`.
- [ ] `buttons/*.jpeg` → PNG with transparent corners.
- [ ] Crop/resize `backgrounds/uropa.png` (typo for "europa", rename) to 800×600.
- [ ] Still to design (placeholders until then): Earth, belt and Jupiter backgrounds; space-junk and ice-chunk (and cracked) sprites; football bullet; pixel heart; ship matching the Hero style.

## #6 — Hero art shows real-world logos `[bug]`

**Status:** open — release blocker for #2

`characters/hero.png` shows the Puma mark and the Egypt FA badge. Kept deliberately for now. Replace or remove before the public itch.io release.
