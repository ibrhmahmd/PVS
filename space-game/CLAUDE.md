# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

"Space X" is an educational space shooter built with Pygame Zero. It is one of three projects in the `PVS/` repo (see `../CLAUDE.md` for the workspace layout and the Delegate-Skills workflow). Work is tracked in the local `ISSUES.md`.

## Commands

- Run: `python Game.py` (needs `pip install pgzero`). There is no build step, test suite or linter.
- Works from any folder: `Game.py` does `os.chdir` to its own folder (or `sys._MEIPASS` when frozen).

## Architecture

Read `CONTEXT.md` first for the terms (Hero, Ship, Mission, Journey, Level, Launch pad, Earth orbit, Checklist, Countdown, Scan, Fact card, Title screen). The code follows the user's "kid-simple" rules: plain functions and loops, no classes or try/except, one small file per screen, repetition over abstraction, short comments in kid words.

`Game.py` stays at the root (Pygame Zero finds `images/`, `music/` and `fonts/` next to it) and holds only the hooks plus `start_level()`. Code lives in four packages, each with an empty `__init__.py` so PyInstaller finds them: `screens/`, `levels/`, `parts/` and `data/`. Import with `from parts import ship`. It switches on `game_states.mode` (`TITLE`, `PLAYING`, `FACT_CARD`, `GAME_OVER`, `WIN`) like Crab-game's `main.py`.

- `parts/game_states.py` is the shared state (`mode`, `level_number`, `score`, `level_points`, `level_cleared`, `health`, `paused`, ...).
- Screens switch by setting a mode. `screens/title.py`, `fact_card.py` and `game_over.py` set the transient modes `NEXT_LEVEL` / `RETRY_LEVEL`, and `Game.update()` turns those into `start_level()` or `win.start()`.
- `data/level_data.py` has `TITLE_STORY`, `LEVELS` (per-Level name, background, points `target` for flying Levels, Fact card `story` and `fact`) and `WIN_STORY`/`WIN_FACT`. Add a Level by adding an entry here, a file in `levels/`, and the module to `LEVEL_FILES` in `Game.py`.
- Each `levels/*.py` exposes `start()`, `update(keyboard)`, `draw(screen)`, `on_key_down(key, keys)` and a `background` Actor. A Level changes `health`, `score` and `level_points`, and sets `game_states.level_cleared = True` when it is finished (points target reached, the Hero boarded, the Scan done). `Game.update()` then shows the Fact card, or game over when `health <= 0`.
- `levels/launch_pad.py` is the odd one: the player walks the Hero (no Ship, no hearts). Running out of Countdown sets `health = 0`, so the normal game-over path handles it. It draws its own top bar and borrows `hud.draw_pause()`.
- `parts/ship.py` (Ship, footballs, auto-fire, shoot sound), `parts/controls.py` (on-screen buttons) and `parts/hud.py` (score, hearts, pause overlay) are shared by the flying Levels.
- `data/game_data.py` is `space_info_list`, the random facts shown at game over.
- `pgzero` 1.2.1 ignores `Actor.scale`, so sprite files are sized as they appear on screen.

## Gotchas

- `screen`, `keyboard`, `keys` and `music` are Pygame Zero builtins that exist only in `Game.py`. Other modules receive `screen` and `keyboard` as arguments and import `keys` from `pgzero.keyboard`.
- `images/` is grouped by role, and `Actor("folder/name")` takes the folder: `backgrounds/` (one per screen), `characters/` (Hero, small Hero, Ship), `sprites/` (asteroid, junk, ice, cracked ice, football), `items/` (the 4 Checklist items), `ui/` (buttons, heart, logo), `planets/` (lowercase names, used by the game-over facts in `data/game_data.py`). Add new art to the matching folder.
- `images/originals/` holds the full-size source art, and `docs/art-prompts.md` has the image-generation prompts plus a status table. The Earth orbit, Jupiter and Title backgrounds and the junk and ice sprites are generated art. `backgrounds/belt.png` is a dimmed copy of `originals/belt.png`, accepted as final. The Launch pad background and the planet pictures are real art (sources in `images/originals/`; Venus is still the old non-pixel picture). The football is real art (32×32 from `originals/football.png`). The Ship views and the heart are kept as they are by decision. Only the 4 Checklist items are still placeholders.
- All text uses the pixel font `fonts/jersey10.ttf` (set once in `Game.py` with `ptext.DEFAULT_FONT_NAME = "jersey10"`; Pygame Zero's font loader wants the bare name, not a path). Every `screen.draw.text` call has `owidth=1.5, ocolor="black"` so text reads over any picture; keep that on new text. `characters/hero_small*.png` are a shrunk and a mirrored copy of `hero.png`.
- `pgzrun` overwrites `__file__` when imported, so `Game.py` sets its folder before `import pgzrun`. Pygame Zero calls `update()` with no keyboard argument (it passes `dt` if `update` takes one), so use the `keyboard` builtin inside `Game.py`.
- `images/characters/hero.png` shows the Puma and Egypt FA logos. `ISSUES.md` #6 blocks the public release.
- Game text and controls are mirrored on the Pixel Verse Studios website. Keep them in sync if you change titles or controls.
