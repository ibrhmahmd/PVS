# The first screen: the Hero sits on the Ship. Press Space (or click) and they fly off.
from pgzero.actor import Actor
from parts import game_states

LAUNCH_SPEED = 6   # pixels per frame while flying up

background = Actor("backgrounds/space_background", (400, 300))
logo = Actor("logo", (400, 95))
hero = Actor("characters/hero", (400, 290))
ship = Actor("characters/ship", (400, 440))
launching = False


def go():
    global launching
    launching = True


def update():
    global launching
    if launching:
        hero.y -= LAUNCH_SPEED
        ship.y -= LAUNCH_SPEED
        if ship.y < -150:
            # Off the top of the screen: start Level 1.
            launching = False
            hero.y = 290
            ship.y = 440
            game_states.mode = "NEXT_LEVEL"


def draw(screen):
    background.draw()
    logo.draw()
    hero.draw()
    ship.draw()
    if not launching:
        screen.draw.text("Journey to Jupiter", center=(400, 520), fontsize=36, color="cyan")
        screen.draw.text("Press Space to launch", center=(400, 565), fontsize=44, color="white")
