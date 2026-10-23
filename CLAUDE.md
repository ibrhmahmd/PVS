# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Workspace layout

`PVS/` is **one git repo** (branch `main`, remote `https://github.com/ibrhmahmd/PVS`) holding three projects for the fictional studio Pixel Verse Studios. Until 2026-10-08 they were separate repos. Their histories were imported under each folder, so `git log -- space-game/` shows only the import merge: use `git log <import-commit>^2` to see a project's older commits. The old `.git` folders are backed up in `../PVS-git-backups/`. The old GitHub repos (`ibrhmahmd/crab-quests`, `ibrhmahmd/pixel-verse-studios`) are no longer pushed to. Each project keeps its own `ISSUES.md`, `.gitignore` and `.gitattributes`; the root `.gitignore` covers `.venv/`, `__pycache__/` and `.claude/worktrees/` everywhere.

| Dir | What | Stack |
|---|---|---|
| `pixel-verse-studios/` | The studio's marketing website | Static HTML + one hand-written CSS file |
| `Crab-game/` | "Crab Quest", a 6-chapter platformer | Python, Pygame Zero |
| `space-game/` | "Space X", an educational space shooter | Python, Pygame Zero |

The root `index.html` is only a redirect to `pixel-verse-studios/index.html` (so the repo root can be served as the site); don't put content there. The root `ISSUES.md` tracks cross-project work (the `docs/` deliverables).

The website describes the two games, so changes to game content/controls/titles must stay consistent with the site (see the "Game content is real" rule in `pixel-verse-studios/CLAUDE.md`). Each project tracks work in a local `ISSUES.md`; the games' packaging issues (PyInstaller + itch.io) are waiting on a Windows 11 build session, and the site's "Play" buttons link to those itch.io pages.

`pixel-verse-studios/` has its own detailed `CLAUDE.md` / `AGENTS.md` (styling loop, per-page rules, design-system gotchas). Read it before touching the site; it is not repeated here.

## Docs (competition deliverables)

`docs/` is the competition showcase kit (built with the `project-showcase` skill): `pvs-documentation.md` + PDF, the 1000×2000 mm poster in `poster/`, the 13-slide deck in `presentation/` (slides 5-8 walk through every level of both games), diagrams in `diagrams/`, and real screenshots in `screenshots/`. Rebuild with `python3 docs/build.py [diagrams|poster|slides|documentation]` (needs Google Chrome and `pip install playwright markdown-it-py`; these are not game dependencies). Yellow "✏️ Student writes" boxes are story lines for the team to write, and `build.py` counts the ones left. The QR code is `docs/assets/qr-app.svg`, made with `qrencode`, and points at `https://ibrhmahmd.github.io/PVS/`. Space X screenshots come from the real game run headless, so recapture them when its look or numbers change. Tracked in `ISSUES.md` #1.

## Commands

**Website** (run from `pixel-verse-studios/`):
- `python3 scripts/check_site.py`: the acceptance check for structural changes (there is no test suite). No build step; styles live in `assets/css/styles.css`.
- `python3 -m http.server 8000`: preview.

**Games** (no tests, no linter; `dependencies = []` in `Crab-game/pyproject.toml`, so `pgzero` is installed manually, `pip install pgzero`, or via the existing `Crab-game/.venv`; space-game pins `pgzero==1.2.1` / `pygame==2.6.1` in `space-game/requirements.txt`):
- `cd Crab-game && python main.py` (or `uv run main.py`)
- `cd space-game && python Game.py`

Both games run from any folder: Pygame Zero loads `images/` and `music/` relative to the entry script. space-game also `os.chdir`s to its own folder because it loads some files with plain pygame.

## Game architecture

**Crab-game**: a mode-dispatch state machine.
- `main.py` is the only Pygame Zero entry point (`pgzrun.go()`). Its `draw`/`update`/`on_mouse_down`/`on_key_down` hooks switch on `game_states.game_mode` (`START_SCREEN`, `LEVEL_SELECT`, `LEVEL1`..`LEVEL6`) and delegate to the matching module's `draw(screen)` / `update(keyboard)` / `on_key_down(key, keys)`.
- `game_states.py` is the shared mutable state (`game_mode`, `is_music_on`, `is_game_over`, `has_won`). Modules switch screens by assigning `game_states.game_mode`.
- Each `level_N.py` is self-contained (own `Actor`s, platforms, physics constants, and a `reset()`). Adding a level means a new module plus a branch in each dispatcher in `main.py` and an entry in `level_select.py`/`start_screen.py`, which import all levels.
- The mute button lives in `main.py` and is drawn over every screen.

**space-game**: "Journey to Jupiter", a mode-dispatch state machine like Crab-game (details in `space-game/CLAUDE.md`; domain terms such as Hero, Ship, Mission, Level are defined in `space-game/CONTEXT.md`, use them).
- `Game.py` holds only the Pygame Zero hooks and switches on `parts/game_states.mode`. Code lives in `screens/`, `levels/` (launch_pad, earth_orbit, belt, europa), `parts/` (ship, controls, hud, state) and `data/` (Level targets, facts).
- Assets load from the game's own folder, so it runs from any directory.

## Conventions

- Both games use Pygame Zero conventions: `Actor("name")` resolves `images/name.png`, and `screen`, `keyboard`, `music` are injected builtins (not imported) in the entry-point module.
- Use of the Delegate-Skills workflow (issue → plan → OpenCode delegation → review → user-approved merge) from the user's global instructions applies here; keep each issue in the relevant project's `ISSUES.md`.
