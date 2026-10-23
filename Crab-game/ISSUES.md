# Issues

## #1 — Package Crab Quest for players `[feature]`

**Status:** open — waiting for the Windows 11 build session

Ship two downloads and publish them on an itch.io page; the Pixel Verse Studios website (`stitch_pixel_verse_visual_identity`, issue #5) links its "Play" buttons there.

- [ ] Windows build with PyInstaller (built on the Windows 11 laptop; bundle `images/` and `music/`)
- [ ] Source zip (`git archive`) with run instructions: install Python + `pip install pgzero`, then `python main.py`
- [ ] itch.io page with screenshots, description, controls, both downloads
- [ ] Smoke-test the .exe on a clean Windows machine (all 6 chapters, music toggle)

## #2 — Gameplay fixes before packaging `[bug]`

**Status:** fixed (verified by a headless play-through)

Found by a headless play-through audit (2026-10-15). No crashes; these are the gameplay problems.

- [x] Level 2: birds never spawn near the edges, so holding Right wins every time. Spawn across the full width.
- [x] Level 3: same edge exploit, and the intended route is nearly unwinnable at `MOVE_SPEED = 3`. Spawn across the full width and raise the speed to 5.
- [x] No way out of a level except winning. ESC goes back to level select from any level (and to the start screen from level select); show a small "ESC: chapters" hint.
- [x] Start/level-select buttons flicker on hover: `start_btn.png` is 150×150, `start_btn_hover.png` is 118×81. Make both the same size.
- [x] Level-select labels show emoji the font can't draw (empty boxes). Use plain text.
- [x] Level 6 has no left/right screen limit.
- [x] Levels 4 and 5: winning and losing in the same frame leaves `is_game_over` set after RETURN. Clear both flags.

Left as is: in levels 1 and 4 the crab can step onto a platform from its side (makes them a bit easier, breaks nothing).
