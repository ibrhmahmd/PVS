# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

"Space X" is an educational space shooter built with Pygame Zero. It is one of three sibling repos under `PVS/` (see `../CLAUDE.md` for the workspace layout and the Delegate-Skills workflow). Work is tracked in the local `ISSUES.md`.

## Commands

- Run: `python Game.py` (needs `pip install pgzero`). There is no build step, test suite or linter.
- Works from any folder: `Game.py` does `os.chdir` to its own folder (or `sys._MEIPASS` when frozen).

## Architecture

Read `CONTEXT.md` first for the terms (Hero, Ship, Journey, Level, Challenge, Fact card, Intro). The code follows the user's "kid-simple" rules: plain functions and loops, no classes or try/except, one small file per screen, repetition over abstraction, short comments in kid words.

`Game.py` stays at the root (Pygame Zero finds `images/` and `music/` next to it) and holds only the hooks plus `start_level()`. Code lives in four packages, each with an empty `__init__.py` so PyInstaller finds them: `screens/`, `levels/`, `parts/` and `data/`. Import with `from parts import ship`. It switches on `game_states.mode` (`INTRO`, `PLAYING`, `FACT_CARD`, `GAME_OVER`, `WIN`) like Crab-game's `main.py`.

- `parts/game_states.py` is the shared state (`mode`, `level_number`, `score`, `level_points`, `health`, `paused`, ...).
- Screens switch by setting a mode. `screens/intro.py`, `fact_card.py` and `game_over.py` set the transient modes `NEXT_LEVEL` / `RETRY_LEVEL`, and `Game.update()` turns those into `start_level()` or `win.start()`.
- `data/level_data.py` has `LEVELS`: per-Level name, background, points target and Fact card text. Add a Level by adding an entry here, a file in `levels/`, and the module to `LEVEL_FILES` in `Game.py`.
- Each `levels/*.py` exposes `start()`, `update(keyboard)`, `draw(screen)`, `on_key_down(key, keys)` and a `background` Actor. A Level only changes `health`, `score` and `level_points`. `Game.update()` checks for game over and the points target.
- `parts/ship.py` (Ship, footballs, auto-fire, shoot sound), `parts/controls.py` (on-screen buttons) and `parts/hud.py` (score, hearts, pause overlay) are shared by all Levels.
- `data/game_data.py` is `space_info_list`, the random facts shown at game over.
- `pgzero` 1.2.1 ignores `Actor.scale`, so sprite files are sized as they appear on screen.

## Gotchas

- `screen`, `keyboard`, `keys` and `music` are Pygame Zero builtins that exist only in `Game.py`. Other modules receive `screen` and `keyboard` as arguments and import `keys` from `pgzero.keyboard`.
- `images/originals/` holds the full-size source art, and `docs/art-prompts.md` has the image-generation prompts for every missing asset. Earth, belt and Jupiter backgrounds and the junk, ice and football sprites are placeholders.
- `images/characters/hero.png` shows the Puma and Egypt FA logos. `ISSUES.md` #6 blocks the public release.
- Game text and controls are mirrored on the Pixel Verse Studios website. Keep them in sync if you change titles or controls.
