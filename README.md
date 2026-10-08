# Space X: Journey to Jupiter

An educational space shooter. The Hero flies from Earth to Jupiter, learning about each place on the way.

## How to play
- **Space**: start / shoot (Asteroid belt and Europa shoot automatically too)
- **Left / Right arrows** or the on-screen arrow buttons: move the Ship
- **P** or the pause button: pause. **F**: fullscreen. **R**: retry after game over.

The Journey: Earth (dodge space junk) → Asteroid belt (shoot asteroids) → Europa (ice chunks need two hits) → Jupiter. Each Level ends when you reach its points target and shows a Fact card.

## How it works
`Game.py` has the Pygame Zero hooks and switches on `game_states.mode`. Every screen and Level has its own small file:

- `screens/`: whole screens (Intro, Fact card, game over, win)
- `levels/`: one file per Level (`earth.py`, `belt.py`, `europa.py`)
- `parts/`: pieces every Level shares (the Ship, buttons, score and hearts, the game state)
- `data/`: Level points targets and facts (`level_data.py`), random game-over facts (`game_data.py`)

Each folder has an empty `__init__.py`, which tells Python (and the Windows build tool) that the folder holds code. Words like Hero, Ship, Level and Fact card are defined in `CONTEXT.md`.

## Run it
```
pip install pgzero
python Game.py
```
Works from any folder; images and music are found next to `Game.py`.

## Limits
- The high score is kept in memory only; it resets when the game closes.
- A missing image or sound crashes the game with an error (no friendly message).
- Points targets are fixed numbers in `data/level_data.py`.
- Europa's ice chunks only have two states: whole, then cracked.
- The Hero art shows real-world logos (Puma, Egypt FA badge). Replace before a public release (ISSUES.md #6).
- `music/shoot.wav` is a generated placeholder beep, and `images/logo.png` is a shrunk copy of `logogame.png`.
- Earth, belt and Jupiter backgrounds, junk, ice and football sprites are placeholders.
