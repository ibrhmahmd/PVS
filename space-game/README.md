# Space X: Journey to Jupiter

An educational space game. The Hero's Mission is to fly to Europa, Jupiter's icy moon, and find out if its hidden ocean could hold life. He learns about each place on the way.

## How to play
- **Left / Right arrows** or the on-screen arrow buttons: walk the Hero (Launch pad) or move the Ship
- **Space**: start / continue / shoot (the Ship also shoots by itself in the Asteroid belt and on Europa)
- **P** or the pause button: pause. **F**: fullscreen. **R**: retry after game over.

The Journey:
1. **Launch pad**: walk to the Ship before the 30-second Countdown ends. Pick up the 4 Checklist items first (helmet, ammo crate, lucky football, fuel can); the door stays shut until you have them all.
2. **Earth orbit**: dodge the space junk.
3. **Asteroid belt**: shoot the asteroids.
4. **Europa**: break the ice chunks (two hits each), then the Ship scans for the hidden ocean.

Then Jupiter: the win screen. Every Level ends with a Fact card: what happens next, and one science fact.

## How it works
`Game.py` has the Pygame Zero hooks and switches on `game_states.mode`. Every screen and Level has its own small file:

- `screens/`: whole screens (Title screen, Fact card, game over, win)
- `levels/`: one file per Level (`launch_pad.py`, `earth_orbit.py`, `belt.py`, `europa.py`)
- `parts/`: pieces the Levels share (the Ship, buttons, score and hearts, the game state)
- `data/`: Level names, points targets, story and facts (`level_data.py`), random game-over facts (`game_data.py`)

Each Level says by itself when it is finished (it sets `level_cleared`), then the Fact card shows. Each folder has an empty `__init__.py`, which tells Python (and the Windows build tool) that the folder holds code. Words like Hero, Ship, Level, Checklist and Fact card are defined in `CONTEXT.md`.

## Run it
```
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python Game.py
```
Works from any folder; images and music are found next to `Game.py`.

## Limits
- The high score is kept in memory only; it resets when the game closes.
- A missing image or sound crashes the game with an error (no friendly message).
- Points targets and the 30-second Countdown are fixed numbers in the code.
- The Hero can't jump on the Launch pad; he only walks left and right, using one picture flipped for each direction (no walking animation).
- Europa's ice chunks only have two states: whole, then cracked. The Scan can't fail.
- The Hero art shows real-world logos (Puma, Egypt FA badge). Replace before a public release (ISSUES.md #6).
- `music/shoot.wav` is a generated placeholder beep, and `images/ui/logo.png` is a shrunk copy of `images/originals/logogame.png`.
- Placeholders: the Launch pad background, the 4 Checklist items, both Ship pictures, the football and the heart. The belt background is a dimmed stand-in until a version without rocks is made.
- The font is Jersey 10 (`fonts/jersey10.ttf`), free under the SIL Open Font License (`fonts/OFL.txt`, which must ship with the game).
