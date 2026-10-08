# Art prompts: Space X, Journey to Jupiter

Detailed image-generation prompts for every asset the game still needs. Each one names the file it replaces, the size it is shown at, and where the game draws text and buttons on top of it (measured from the code), so nothing important ends up hidden.

**Already final, don't regenerate:** the Hero (`characters/hero.png`), the Europa background, the asteroid, the 4 buttons, the logo and the 10 planet images used on the game-over screen.

---

## How to use these prompts

1. **Attach two style references to every generation:** `images/originals/hero.png` (the astronaut) and `images/originals/uropa.png` (the Europa landscape). They define the look. Everything new must look like it comes from the same game.
2. **Paste the Style block below in front of every prompt.** Then paste the Sprite block (for objects) or the Background block (for full scenes), then the asset's own prompt.
3. **Generate big; I shrink.** Backgrounds at **1600×1200** (or any 4:3 size). Sprites at **1024×1024**. I cut out the background, resize to the exact size and wire the file into the game.
4. **Some assets are generated together on one sheet** (marked **Sheet**), so they come out matching. I split the sheet into separate files.
5. **Put the results in `images/originals/new/`** with the file name from the heading and tell me. If you only get a JPEG, that's fine for backgrounds. Sprites need the flat magenta background described below.

### Style block (all images)

> 16-bit retro pixel art in the exact style of the attached reference images. Crisp, hard-edged square pixels, no anti-aliasing, no blur, no smooth gradients (shading is done with 3 to 5 stepped pixel tones). Rich but limited palette: deep navy and black for space, icy blues and whites, warm oranges and creams, bold reds. Every object has a dark 1 to 2 pixel outline (near-black navy, not pure black). Light comes from the upper left. Clean and readable for children. Large, chunky pixels: the image should look like it was drawn at a quarter of its size and scaled up 4×.

### Sprite block (single objects and sheets)

> The object is centred and fills about 80% of the frame. The background is one perfectly flat, solid magenta colour (#FF00FF) with no texture, no gradient, no shadow and no floor. Nothing touches the edges of the image. No magenta inside the object itself.

### Background block (full scenes)

> A full-frame 4:3 landscape scene with no characters and no spaceships in it. Keep the areas described as "calm" low in detail and slightly darker, because the game draws text and moving objects on top of them.

### Avoid (add to every prompt, or to the negative prompt if your tool has one)

> No text, no letters, no numbers, no logos, no watermark, no signature, no UI, no border or frame, no photo-realism, no 3D render look, no smooth vector art, no blurry or soft edges, no lens flare, no extra characters.

---

## Backgrounds (shown at 800×600)

Where the game draws on top of the flying Levels (Earth orbit, Asteroid belt):

- **Top strip (y 0–90):** score top-left, Level name and points top-centre, hearts top-right. Keep it calm and dark.
- **Middle (y 90–420):** asteroids, junk or ice fall down through here. Medium-low detail so the falling sprites stand out.
- **Bottom strip (y 420–600):** the Ship flies left and right at y≈470, with arrow buttons in the bottom-left corner and a pause button bottom-right. Keep it calm.

### 1. `backgrounds/launch_pad.png`: Level 1, Launch pad

> Side view, like a 2D platform game, of a sunny rocket launch station on Earth in the daytime. The ground is a flat, light-grey concrete launch pad running across the whole width of the bottom of the image. Its top edge is perfectly straight and horizontal at exactly 5/6 of the image height (y=500 of 600), with a thin yellow-and-black safety stripe along that edge and faint square concrete slab lines below it. Above the ground: a bright cheerful blue sky, lighter towards the horizon, with three or four puffy white pixel clouds. Far in the distance behind the pad: soft green rolling hills, a few palm trees and a small white mission-control building with a satellite dish and a red-and-white striped radio mast, all small and slightly faded to look far away. On the far right edge of the image (the last 1/20 of the width), a tall red-and-white steel launch tower made of criss-cross girders rises from the pad to about 2/3 of the image height, with a small gantry arm pointing left. Leave the whole middle and right part of the pad empty and uncluttered: a walking astronaut and a big upright spaceship are drawn there by the game. No rocket, no ship and no people in the picture. Happy, bright, adventurous mood, the moment before a launch.

Layout notes: the Hero walks between x 50 and 560 standing on the line at y=500 (his head reaches y≈360). The Ship stands at x 590–770 on the same line. A Countdown and a checklist bar sit across the top 70 px; keep the sky there plain.

### 2. `backgrounds/earth.png`: Level 2, Earth orbit

> View from low Earth orbit looking out over our planet. The curved edge of the Earth fills the bottom quarter of the image as a wide, gentle arc that rises from the bottom-left corner, peaks in the middle at about 4/5 of the image height, and falls to the bottom-right corner. On the planet: deep blue oceans, the green and sandy-brown shape of North Africa and the Nile valley, swirls of white clouds, and a thin glowing light-blue band of atmosphere along the curved edge. Above it, deep black-navy space with scattered tiny white and pale-blue stars of different sizes, and a faint distant Moon, small and grey, in the upper-left area. Two or three very small, far-away satellites glint as tiny white specks. The space area above the Earth stays dark and calm for the falling space junk. This must look clearly different from the purple nebula title screen: here it is black space, the blue Earth and no nebula.

### 3. `backgrounds/belt.png`: Level 3, Asteroid belt

> Deep space inside the asteroid belt between Mars and Jupiter. A faint, wide band of dusty brown-gold haze, like fine glittering dust, crosses the image diagonally from the lower-left to the upper-right. The band is made only of soft dust and tiny single-pixel specks; there are NO rocks, NO stones and NO asteroids anywhere in the picture (the game draws its own asteroids on top, and any rock in the background would confuse the player). In the top-left corner, a small reddish-orange Mars, about 1/12 of the image width. In the top-right corner, the Sun as a small bright white-yellow star with a soft pixel glow. The rest is dark navy-black space with sparse stars. Overall dark and low in contrast, so bright moving objects stand out. Moody and mysterious, not cluttered.

Add to the Avoid list for this one: no asteroids, no rocks, no boulders, no stones, no planets except Mars.

(The first version had big outlined rocks that looked just like the game's asteroids. Until a new one is made, the game uses that version dimmed.)

### 4. `backgrounds/jupiter.png`: Win screen

> A triumphant, celebratory view of the planet Jupiter, enormous, its round body filling the right half of the image and running off the right and bottom edges. Clearly banded clouds in horizontal stripes of cream, tan, light orange, rusty brown and white, with soft swirling edges between the bands, and the Great Red Spot, a big oval red-orange storm, clearly visible in the lower-right part of the planet. Two of Jupiter's moons float nearby: one small icy white-blue moon with faint brown crack lines (Europa) on the upper-left of Jupiter, and one small orange-yellow speckled moon (Io) farther left. The left third of the image is deep navy space with bright stars and a few warm golden sparkles, like a celebration. Warm sunlight from the upper left lights the planet's left side, and the right edge falls into shadow.

Layout notes: the Hero stands at the left (x 75–205, y 230–430). A dark text panel covers x 245–755, y 115–345, and big text sits at the top (y≈60) and bottom (y 430–560). Jupiter's banding and the Great Red Spot should be visible around and below the panel, especially on the right and bottom-right.

### 5. `backgrounds/space_background.png`: Title screen (optional, replaces the current one)

> A rich, poster-like deep-space scene for a game's title screen. A soft swirl of purple, magenta and blue nebula clouds fills the background, brightest around the centre and fading to dark navy at the corners. A tiny blue Earth in the lower-left corner and a tiny banded Jupiter in the upper-right corner, both far away, suggest the journey from one to the other, with a faint dotted line of light between them. Scattered bright stars and two or three twinkling 4-point star sparkles. The centre column of the image stays calm and slightly darker: a logo sits at the top and the astronaut stands in the middle.

Layout notes: the logo covers x 315–485, y 10–180, the Hero x 335–465, y 200–400, story text y 415–470, high score y≈505 and "Press Space to start" y≈560.

---

## Sprites

### 6. Sheet: `characters/ship.png` + `characters/ship_pad.png`, the Ship in two views

Generate both views on **one image, side by side**, so they're obviously the same ship. I split them.

> A character sheet showing the same small, friendly, rounded spaceship in two views side by side on the magenta background, with a clear gap between them. The design: a white hull with bold red stripes (matching the red-and-white suit of the attached astronaut), a big round light-blue glass cockpit window near the nose, two short swept-back wings with red tips, a small Egyptian flag decal (red, white and black horizontal stripes) on one wing, and a single round engine nozzle at the back. LEFT VIEW: the ship seen from directly above, nose pointing straight up, perfectly symmetrical left and right, with a short bright blue-white engine flame coming out of the bottom. RIGHT VIEW: the same ship standing upright on the ground, seen from the side, nose pointing up, resting on three short landing legs, with a small open hatch door and a little 3-step ladder at the bottom of the hull, and no flame (the engine is off).

Shown at: `ship.png` 100×100 (flying, top-down) and `ship_pad.png` 180×180 (standing on the Launch pad).

### 7. Sheet: `item_helmet.png`, `item_ammo.png`, `item_football.png`, `item_fuel.png`, the Checklist

> A sprite sheet of 4 separate game pickup items in one horizontal row on the magenta background, evenly spaced with clear gaps between them, all the same size, each one bold and simple enough to read at a tiny size: (1) a white astronaut space helmet seen from the front, with a dark-blue reflective visor, a small white shine on the visor and a thin red stripe around the rim, matching the attached astronaut's helmet; (2) a small wooden supply crate with darker wood planks and metal corner brackets, its lid open and leaning back, filled with three black-and-white footballs (soccer balls) poking out; (3) a single classic black-and-white football (soccer ball) with pentagon panels and a tiny gold star sticker on it, the astronaut's lucky ball; (4) a red metal fuel can (jerry can) with a black screw cap on top, a handle, and a yellow lightning-bolt stripe on the side.

Shown at: 48×48 each, both on the ground and as icons in the checklist bar.

### 8. `junk.png`: space junk (Earth orbit)

> An old, broken, tumbling satellite drifting in space, seen from the side at a slight angle: a dented grey-silver box-shaped body with scratches, a few loose bolts and a small dish antenna, two rectangular dark-blue solar panel wings with a grid of cells, one wing bent and cracked, and a short snapped-off antenna rod. A couple of tiny metal fragments float near it. It should look old, abandoned and dangerous, but simple and readable.

Shown at: about 100×60 (wide, not tall). Make it wider than it is tall.

### 9. Sheet: `ice.png` + `ice_cracked.png`, the Europa ice chunk

Generate both on **one image, side by side**, so the shape matches exactly.

> Two versions of the same chunk of Europa ice, side by side on the magenta background with a clear gap. The chunk: a jagged, roughly round, faceted lump of frozen ice like a crystal rock, pale icy blue and white with lighter frosty edges on the top-left, darker blue facets on the bottom-right, a few thin rusty-brown streaks (like Europa's surface lines), and a bold dark-navy outline so it stands out against a white-and-blue icy background. LEFT: whole and undamaged. RIGHT: exactly the same chunk (same shape, same size, same colours) but hit once: a big dark zig-zag crack runs across it from top to bottom, two small shards are breaking off one edge, and a few tiny ice flakes are flying away.

Shown at: about 95×90 each.

### 10. `football.png`: the Ship's bullet

> A single classic football (soccer ball), perfectly round, white with black pentagon panels in the traditional pattern, a small bright white shine on the upper left, and a short faint white speed trail behind it pointing straight down (it is flying upwards). Very bold and simple: it must read clearly at a tiny size.

Shown at: 32×32. Keep the trail short so the ball itself fills most of the frame.

### 11. `health.png`: a heart (lives)

> A single shiny, chunky, classic video-game heart for showing lives: bright red with a darker red shade on the lower right, a small white square shine on the upper left, and a bold dark outline.

Shown at: about 32×32, in a row of three at the top right.

---

## Optional

### 12. `fact_card_frame.png`: Fact card frame (720×480)

> A flat, front-facing sci-fi panel frame for a game's information card: a dark navy-blue rounded rectangle, plain and empty in the middle (text goes there), with a glowing cyan metal border about 1/30 of the width thick, small rivets in all four corners, and a little decorative tab at the top centre. Nothing inside the panel.

### 13. `characters/hero_clean.png`: the Hero without real-world logos (for the public release, ISSUES.md #6)

> Exactly the same astronaut as the attached reference: same face, pose, suit, colours, helmet, gloves, football and size. The only differences: remove the sportswear brand logo on the trousers, and replace the football-federation badge on the chest with a simple round mission patch showing a small rocket and a star. Keep the Egypt flag patches, the number 16 and the red-and-white design.

### 14. `characters/hero_walk.png`: a walking pose (only if you want a 2-frame walk)

> Exactly the same astronaut as the attached reference, same style, colours and size, seen from the side and walking to the right in mid-stride: one leg forward, one leg back, arms swinging, the football tucked under one arm.

---

## Checklist of files

| # | File | Shown at | Generated as | Status |
|---|---|---|---|---|
| 1 | `backgrounds/launch_pad.png` | 800×600 | single | to do |
| 2 | `backgrounds/earth.png` | 800×600 | single | done |
| 3 | `backgrounds/belt.png` | 800×600 | single | redo with the new prompt (dimmed for now) |
| 4 | `backgrounds/jupiter.png` | 800×600 | single | done |
| 5 | `backgrounds/space_background.png` (optional) | 800×600 | single | done |
| 6 | `characters/ship.png` + `characters/ship_pad.png` | 100×100 + 180×180 | sheet of 2 | to do |
| 7 | `item_helmet.png`, `item_ammo.png`, `item_football.png`, `item_fuel.png` | 48×48 each | sheet of 4 | to do |
| 8 | `junk.png` | ~100×60 | single | done |
| 9 | `ice.png` + `ice_cracked.png` | ~95×90 each | sheet of 2 | done |
| 10 | `football.png` | 32×32 | single | to do |
| 11 | `health.png` | ~32×32 | single | to do |
| 12 | `fact_card_frame.png` (optional) | 720×480 | single | to do |
| 13 | `characters/hero_clean.png` (optional, release) | 131×200 | single | to do |
| 14 | `characters/hero_walk.png` (optional) | 92×140 | single | to do |
