# Space X: Journey to Jupiter

An educational space shooter. The Hero flies from Earth to Jupiter, learning about each place on the way.

## How to play
- **Space**: start / shoot (Asteroid belt and Europa shoot automatically too)
- **Left / Right arrows** or the on-screen arrow buttons: move the Ship
- **P** or the pause button: pause. **F**: fullscreen. **R**: retry after game over.

The Journey: Earth (dodge space junk) → Asteroid belt (shoot asteroids) → Europa (ice chunks need two hits) → Jupiter. Each Level ends when you reach its points target and shows a Fact card.

## How it works
`Game.py` has the Pygame Zero hooks and switches on `game_states.mode`. Every screen and Level has its own small file (`intro.py`, `level_earth.py`, `fact_card.py`, ...). Level points targets and facts are in `level_data.py`; the random game-over facts are in `game_data.py`. Words like Hero, Ship, Level and Fact card are defined in `CONTEXT.md`.

## Run it
```
pip install pgzero
python Game.py
```
Works from any folder; images and music are found next to `Game.py`.

## Limits
- The high score is kept in memory only; it resets when the game closes.
- A missing image or sound crashes the game with an error (no friendly message).
- Points targets are fixed numbers in `level_data.py`.
- Europa's ice chunks only have two states: whole, then cracked.
- The Hero art shows real-world logos (Puma, Egypt FA badge). Replace before a public release (ISSUES.md #6).
- Earth, belt and Jupiter backgrounds, junk, ice and football sprites are placeholders.
