# The first screen: the Hero sits on the Ship. Press Space (or click) and they fly off.
from pgzero.actor import Actor
import game_states

LAUNCH_SPEED = 6   # pixels per frame while flying up

background = Actor("backgrounds/space_background", (400, 300))
hero = Actor("characters/hero", (400, 260))
ship = Actor("characters/ship", (400, 410))
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
            hero.y = 260
            ship.y = 410
            game_states.mode = "NEXT_LEVEL"


def draw(screen):
    background.draw()
    screen.draw.text("SPACE X", center=(400, 50), fontsize=90, color="yellow")
    screen.draw.text("Journey to Jupiter", center=(400, 110), fontsize=40, color="cyan")
    hero.draw()
    ship.draw()
    if not launching:
        screen.draw.text("Press Space to launch", center=(400, 550), fontsize=50, color="white")
