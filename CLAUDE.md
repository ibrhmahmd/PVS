# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Workspace layout

`PVS/` is **not a git repo itself**. It is a parent folder holding three independent repos (each with its own `.git`, `ISSUES.md`, and `.gitattributes`) for the fictional studio Pixel Verse Studios. Run git commands from inside the sub-project.

| Dir | What | Stack |
|---|---|---|
| `pixel-verse-studios/` | The studio's marketing website | Static HTML + one hand-written CSS file |
| `Crab-game/` | "Crab Quest", a 6-chapter platformer | Python, Pygame Zero |
| `space-game/` | "Space X", an educational space shooter | Python, Pygame Zero |

The website describes the two games, so changes to game content/controls/titles must stay consistent with the site (see the "Game content is real" rule in `pixel-verse-studios/CLAUDE.md`). Each project tracks work in a local `ISSUES.md`; the games' packaging issues (PyInstaller + itch.io) are waiting on a Windows 11 build session, and the site's "Play" buttons link to those itch.io pages.

`pixel-verse-studios/` has its own detailed `CLAUDE.md` / `AGENTS.md` (styling loop, per-page rules, design-system gotchas). Read it before touching the site; it is not repeated here.

## Commands

**Website** (run from `pixel-verse-studios/`):
- `python3 scripts/check_site.py`: the acceptance check for structural changes (there is no test suite). No build step; styles live in `assets/css/styles.css`.
- `python3 -m http.server 8000`: preview.

**Games** (no tests, no linter; `dependencies = []` in `Crab-game/pyproject.toml`, so `pgzero` is installed manually, `pip install pgzero`, or via the existing `Crab-game/.venv`):
- `cd Crab-game && python main.py` (or `uv run main.py`)
- `cd space-game && python Game.py`

Crab-game loads assets with cwd-relative paths (`images/`, `music/`), so launch it from its own folder. space-game fixed this (`os.chdir` to its own folder).

## Game architecture

**Crab-game**: a mode-dispatch state machine.
- `main.py` is the only Pygame Zero entry point (`pgzrun.go()`). Its `draw`/`update`/`on_mouse_down`/`on_key_down` hooks switch on `game_states.game_mode` (`START_SCREEN`, `LEVEL_SELECT`, `LEVEL1`..`LEVEL6`) and delegate to the matching module's `draw(screen)` / `update(keyboard)` / `on_key_down(key, keys)`.
- `game_states.py` is the shared mutable state (`game_mode`, `is_music_on`, `is_game_over`, `has_won`). Modules switch screens by assigning `game_states.game_mode`.
- Each `level_N.py` is self-contained (own `Actor`s, platforms, physics constants, and a `reset()`). Adding a level means a new module plus a branch in each dispatcher in `main.py` and an entry in `level_select.py`/`start_screen.py`, which import all levels.
- The mute button lives in `main.py` and is drawn over every screen.

**space-game**: "Journey to Jupiter", a mode-dispatch state machine like Crab-game (details in `space-game/CLAUDE.md`).
- `Game.py` holds only the Pygame Zero hooks and switches on `parts/game_states.mode`. Code lives in `screens/`, `levels/` (earth, belt, europa), `parts/` (ship, controls, hud, state) and `data/` (Level targets, facts).
- Assets load from the game's own folder, so it runs from any directory.

## Conventions

- Both games use Pygame Zero conventions: `Actor("name")` resolves `images/name.png`, and `screen`, `keyboard`, `music` are injected builtins (not imported) in the entry-point module.
- Use of the Delegate-Skills workflow (issue → plan → OpenCode delegation → review → user-approved merge) from the user's global instructions applies here; keep each issue in the relevant project's `ISSUES.md`.
