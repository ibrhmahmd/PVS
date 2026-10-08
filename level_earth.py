# Level 1: Earth. Dodge the space junk. The Ship cannot shoot here.
import random
from pgzero.actor import Actor
import game_states
import ship
import hud

JUNK_SPEED = 4         # pixels per frame
SPAWN_EVERY = 45       # frames between new pieces of junk (a bit under one a second)

background = Actor("backgrounds/earth", (400, 300))
junk_pieces = []
timer = 0


def start():
    global timer
    junk_pieces.clear()
    timer = 0
    ship.reset()


def update(keyboard):
    global timer
    ship.move(keyboard)

    timer += 1
    if timer > SPAWN_EVERY:
        junk = Actor("junk")
        junk.pos = (random.randint(60, 740), -50)
        junk_pieces.append(junk)
        timer = 0

    for junk in junk_pieces[:]:
        junk.y += JUNK_SPEED
        if junk.colliderect(ship.ship):
            ship.play_crash_sound()
            game_states.health -= 1
            junk_pieces.remove(junk)
        elif junk.y > 650:
            # The junk flew past, so we dodged it. That is a point!
            game_states.score += 1
            game_states.level_points += 1
            junk_pieces.remove(junk)


def draw(screen):
    background.draw()
    for junk in junk_pieces:
        junk.draw()
    ship.draw()
    hud.draw(screen)


def on_key_down(key, keys):
    pass  # no shooting on Earth
