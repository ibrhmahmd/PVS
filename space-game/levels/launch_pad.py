# Level 1: Launch pad. Walk the Hero to the Ship before the Countdown ends.
# On the way, pick up the 4 Checklist items. The Ship's door only opens when you have all 4.
import random
from pgzero.actor import Actor
from pygame import Rect
from parts import game_states
from parts import controls
from parts import hud

COUNTDOWN_SECONDS = 30   # time to grab everything and climb in
WALK_SPEED = 5           # pixels per frame
GROUND_Y = 500           # where the concrete starts in the background picture
BLAST_OFF_SPEED = 7      # pixels per frame while the Ship flies up
HERO_START_X = 250
NEXT_TO_SHIP_X = 545     # the Hero is standing next to the Ship's door from here on
FARTHEST_X = 560         # the Hero can't walk into the Ship

# Each item lands somewhere inside its own zone (left x, right x), so the items are always spread out.
# The first zone is behind where the Hero starts, so he has to turn back once.
ZONES = [(60, 180), (320, 410), (430, 500), (515, 560)]
ITEM_NAMES = ["item_helmet", "item_ammo", "item_football", "item_fuel"]

background = Actor("backgrounds/launch_pad", (400, 300))
hero = Actor("characters/hero_small", (HERO_START_X, GROUND_Y - 70))
ship = Actor("characters/ship_pad", (680, GROUND_Y - 90))

# The 4 small pictures at the top that show what you have collected
icons = []
for i in range(4):
    icons.append(Actor(ITEM_NAMES[i], (40 + i * 58, 40)))

items = []         # items still lying on the ground
collected = []     # names of the items the Hero has picked up
frames_left = 0
boarding = False


def start():
    global frames_left, boarding
    hero.image = "characters/hero_small"
    hero.pos = (HERO_START_X, GROUND_Y - 70)
    ship.pos = (680, GROUND_Y - 90)
    frames_left = COUNTDOWN_SECONDS * 60   # the game runs at 60 frames a second
    boarding = False
    collected.clear()
    items.clear()
    # Mix up which item goes in which zone, then drop each one at a random spot inside its zone.
    names = ITEM_NAMES[:]
    random.shuffle(names)
    for i in range(4):
        left, right = ZONES[i]
        item = Actor(names[i], (random.randint(left, right), GROUND_Y - 24))
        item.name = names[i]
        items.append(item)


def update(keyboard):
    global frames_left, boarding
    if boarding:
        ship.y -= BLAST_OFF_SPEED
        if ship.y < -150:
            game_states.level_cleared = True
        return

    frames_left -= 1
    if frames_left <= 0:
        # Too late: the Ship had to launch without the Hero. That counts as losing the Level.
        game_states.health = 0
        return

    if (keyboard.left or controls.held == "left") and hero.x > 50:
        hero.x -= WALK_SPEED
        hero.image = "characters/hero_small_left"
    if (keyboard.right or controls.held == "right") and hero.x < FARTHEST_X:
        hero.x += WALK_SPEED
        hero.image = "characters/hero_small"

    for item in items[:]:
        if hero.colliderect(item):
            collected.append(item.name)
            items.remove(item)
            game_states.score += 1
            game_states.level_points += 1

    # Next to the Ship with all 4 items: climb in and blast off!
    if hero.x >= NEXT_TO_SHIP_X and len(collected) == 4:
        boarding = True


def draw(screen):
    background.draw()
    ship.draw()
    for item in items:
        item.draw()
    if not boarding:
        hero.draw()

    # The Checklist at the top left: an empty box until the item is collected
    for i in range(4):
        screen.draw.rect(Rect(icons[i].x - 26, 14, 52, 52), "white")
        if ITEM_NAMES[i] in collected:
            icons[i].draw()

    # The Countdown. (frames_left + 59) // 60 rounds up, so it shows 30 at the start, not 29.
    seconds = (frames_left + 59) // 60
    color = "white"
    if seconds <= 10:
        color = "red"   # hurry!
    screen.draw.text(f"T-{seconds}", midtop=(400, 10), fontsize=70, color=color, owidth=1.5, ocolor="black")
    screen.draw.text("Level 1: Launch pad", midtop=(400, 65), fontsize=30, color="white", owidth=1.5, ocolor="black")
    screen.draw.text(f"Score: {game_states.score}", topright=(780, 20), fontsize=40, color="yellow", owidth=1.5, ocolor="black")

    if hero.x >= NEXT_TO_SHIP_X and len(collected) < 4:
        screen.draw.text("Checklist not done!", center=(400, 200), fontsize=50, color="orange", owidth=1.5, ocolor="black")

    controls.draw_buttons()
    hud.draw_pause(screen)


def on_key_down(key, keys):
    pass  # no shooting on the Launch pad
