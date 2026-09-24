# Issues

## #1 — Asset paths break when started from another folder `[bug]`

**Status:** open — scheduled for the Windows 11 build session

`Game.py` loads files with cwd-relative paths: `pygame.image.load(current_planet_info["image"])` (paths like `images/Sun.png` from `game_data.py`) and `pygame.mixer.Sound('music/crash.mp3')`. Running the game from any other directory — or from a PyInstaller build — fails to find them. Resolve paths against the game's own folder (and `sys._MEIPASS` when frozen).

## #2 — Package Space X for players `[feature]`

**Status:** open — blocked by #1; waiting for the Windows 11 build session

- [ ] Windows build with PyInstaller (bundle `images/` and `music/`)
- [ ] Source zip with run instructions: install Python + `pip install pgzero`, then `python Game.py`
- [ ] itch.io page with screenshots, description, controls, both downloads
- [ ] Smoke-test the .exe on Windows (start, shoot, game over + planet fact, restart, pause, fullscreen toggle)

The Pixel Verse Studios website (issue #5) links its "Play" buttons to the itch.io page.

## #3 — Typo in the Jupiter fact `[bug]`

**Status:** open

`game_data.py` Jupiter text reads "Great Red Spot, a giant s-torm." — should be "storm".
