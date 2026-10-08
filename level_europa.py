# Level 3: Europa. Shoot the ice chunks. Each chunk needs TWO hits: the first one cracks it.
import random
from pgzero.actor import Actor
import game_states
import ship
import hud

CHUNK_SPEED = 2.5      # slower than asteroids, because chunks are tougher
SPAWN_EVERY = 80       # frames between ice chunks

background = Actor("backgrounds/europa", (400, 300))
chunks = []
timer = 0


def start():
    global timer
    chunks.clear()
    timer = 0
    ship.reset()


def update(keyboard):
    global timer
    ship.move(keyboard)
    ship.update_bullets(auto_fire=True)

    timer += 1
    if timer > SPAWN_EVERY:
        chunk = Actor("ice")
        chunk.pos = (random.randint(60, 740), -50)
        chunk.hits = 0  # how many times it has been shot
        chunks.append(chunk)
        timer = 0

    for chunk in chunks[:]:
        chunk.y += CHUNK_SPEED
        if chunk.colliderect(ship.ship):
            ship.play_crash_sound()
            game_states.health -= 1
            chunks.remove(chunk)
        elif chunk.y > 650:
            game_states.health -= 1
            chunks.remove(chunk)
        else:
            for bullet in ship.bullets[:]:
                if chunk.colliderect(bullet):
                    ship.bullets.remove(bullet)
                    chunk.hits += 1
                    if chunk.hits == 1:
                        chunk.image = "ice_cracked"
                    else:
                        game_states.score += 1
                        game_states.level_points += 1
                        chunks.remove(chunk)
                    break


def draw(screen):
    background.draw()
    for chunk in chunks:
        chunk.draw()
    ship.draw()
    hud.draw(screen)


def on_key_down(key, keys):
    if key == keys.SPACE:
        ship.fire()
