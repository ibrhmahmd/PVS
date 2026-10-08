# Art prompts

Prompts for every missing image, written to match the Hero (`images/originals/hero.png`) and Europa (`images/originals/uropa.png`). Attach both as style references when your tool allows it.

Paste the **style line** in front of every prompt. After generating, drop the file in `images/originals/` and the game-side version is cut out, resized and saved under the name in the heading.

**Style line (all images):**
> 16-bit pixel art, crisp hard-edged square pixels, limited rich palette, dark 1–2 pixel outline around objects, soft pixel shading, same art style as the attached astronaut and Europa images. No text, no letters, no watermark, no border.

**Sprite rule (all sprites, not backgrounds):**
> One single object, centred, filling about 80% of the frame, on a perfectly flat solid magenta (#FF00FF) background. No shadow, no ground, no other objects.

## Backgrounds (800×600, landscape 4:3)

The top 100 px holds the score and Level name, and the bottom 120 px holds the Ship and buttons. Keep those strips calm and darker.

### `backgrounds/earth.png`: Level 1, Earth

> Wide landscape 4:3 view from low Earth orbit. The curved edge of planet Earth fills the bottom quarter of the image: blue oceans, green-brown continents, white cloud swirls and a thin glowing blue atmosphere line. Above it, black space with small stars. A few tiny distant satellites glint in the sky. The top and bottom edges are calm and dark so text can sit on them.

### `backgrounds/belt.png`: Level 2, Asteroid belt

> Wide landscape 4:3 deep-space scene inside the asteroid belt between Mars and Jupiter. Dozens of small and medium brown-grey rocky asteroids drift far away in the background, scattered thinly with lots of empty space between them. A small red Mars far away in one corner, the Sun as a bright small star. Dark blue-black space, faint dust band crossing the scene. Keep the centre fairly open.

### `backgrounds/jupiter.png`: win screen

> Wide landscape 4:3 triumphant view of the planet Jupiter, very large, filling the right two-thirds of the image, with orange, cream and brown cloud bands and the Great Red Spot clearly visible. Two or three of its small moons nearby (one icy white-blue for Europa). Starry black space on the left third, which stays fairly empty for text. Warm, celebratory lighting.

### `backgrounds/space_background.png`: Intro (optional, replaces the original)

> Wide landscape 4:3 starry deep-space scene with a soft purple-blue nebula and a distant galaxy, small Earth visible in the lower left corner. Calm, dark centre where a character will stand.

## Sprites

### `junk.png`: space junk (Earth Level), shown about 100×60

> An old broken satellite seen from the side: a grey-silver box body with dents and two blue solar panel wings, one wing bent, a small antenna. Looks like space junk, slightly worn.

### `ice.png`: ice chunk (Europa Level), shown about 90 px tall

> A jagged chunk of pale blue Europa ice, faceted like a crystal rock, with lighter frosty edges and darker blue cracks inside. Strong dark outline so it stands out on a white-blue icy background.

### `ice_cracked.png`: cracked ice chunk, same size as `ice.png`

> Exactly the same ice chunk as the attached image, same shape, colours and size, but with a big dark crack running across it and a couple of small pieces chipping off the edge. (Attach your `ice.png` result as the reference.)

### `football.png`: the bullet, shown about 32×32

> A classic black-and-white football (soccer ball), round, with pentagon panels, small bright highlight in the top left. Simple and readable at very small size.

### `characters/ship.png`: the Ship, shown 100×100, pointing up

> A small cute spaceship seen from directly above/behind, pointing straight up, white hull with red stripes like the astronaut's suit, a round cockpit window, two small wings and a glowing blue engine flame at the bottom. Symmetrical.

### `health.png`: heart, shown about 28×28

> A single shiny red pixel-art heart with a white highlight, like a classic game life icon.

## Optional

### Fact card frame, shown 720×480

> A sci-fi pixel-art panel frame: dark navy-blue rounded rectangle with a glowing cyan metal border and small rivets in the corners, empty and plain in the middle. Flat front view.
