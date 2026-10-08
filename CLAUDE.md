# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

"Space X" is an educational space shooter built with Pygame Zero. It is one of three sibling repos under `PVS/` (see `../CLAUDE.md` for the workspace layout and the Delegate-Skills workflow). Work is tracked in the local `ISSUES.md`.

## Commands

- Run: `python Game.py` (needs `pip install pgzero`). There is no build step, test suite or linter.
- Run it from this directory. `images/` and `music/` are cwd-relative (`ISSUES.md` #1).

## Architecture

All game code is in `Game.py`, and `pgzrun.go()` at the bottom starts it. State lives in module globals, and every hook that mutates it declares them with `global`. Add any new state variable to the `global` lines in both `update()` and `on_key_down()` and to the reset block under `keys.R`.

- `pgzrun` is imported, but `screen`, `keyboard`, `keys` and `music` are Pygame Zero builtins injected at run time. Don't import them, and expect linters to flag them as undefined.
- `draw()` and `update()` branch on the same flags: `game_started`, `paused`, and `health <= 0`.
  - Game over is `health <= 0`. On the first game-over frame, `update()` picks a random entry from `space_info_list`, loads its image with `pygame.image.load`, and sets `show_info_screen`. `draw()` then renders the fact screen.
  - `R` restarts by resetting the globals inline. There is no `reset()` function.
- `game_data.py` is `space_info_list`, a list of `{"image": "images/X.png", "text": [lines]}` dicts. The lines are joined with spaces for display, so each entry needs a matching file in `images/`.
- Difficulty is derived from `score`, not from `level`. `level = 1 + score // 30` is display-only. Spawn interval (`max(20, 60 - score/2)` frames) and asteroid speed (`3 + min(score/10, 5)`) are computed inline in `update()`.
- Audio: `music.play('music.mp3')` goes through Pygame Zero's music, and `update()` restarts it whenever it isn't playing. The crash sound bypasses Pygame Zero and calls `pygame.mixer.Sound('music/crash.mp3')` on every collision.

## Gotchas

- The `FULLSCREEN` constant is unused. `F` calls `pygame.display.toggle_fullscreen()`.
- `music.stop()` is called from `draw()` while paused. `update()` returns early while paused, so the music only restarts after unpausing.
- The commented-out block in `update()` is a deliberately disabled forward/backward movement feature.
- Game text and controls are mirrored on the Pixel Verse Studios website. Keep them in sync if you change titles or controls: Left/Right to move, Space to shoot or start, P to pause, R to restart, F for fullscreen.
- `Afro-Asian Doc Template.md` is an unrelated school document.
