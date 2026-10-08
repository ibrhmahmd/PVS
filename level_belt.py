# Level 2: Asteroid belt. Shoot the asteroids. This is the only Level with asteroids.
import random
from pgzero.actor import Actor
import game_states
import ship
import hud

BASE_SPEED = 3         # pixels per frame at the start of the Level
SPAWN_EVERY = 60       # frames between asteroids at the start; it gets faster as you score

background = Actor("backgrounds/belt", (400, 300))
asteroids = []
timer = 0


def start():
    global timer
    asteroids.clear()
    timer = 0
    ship.reset()


def update(keyboard):
    global timer
    ship.move(keyboard)
    ship.update_bullets(auto_fire=True)

    timer += 1
    spawn_time = max(25, SPAWN_EVERY - game_states.level_points * 2)
    if timer > spawn_time:
        asteroid = Actor("asteroid")
        asteroid.pos = (random.randint(60, 740), -50)
        asteroids.append(asteroid)
        timer = 0

    speed = BASE_SPEED + min(game_states.level_points / 5, 3)
    for asteroid in asteroids[:]:
        asteroid.y += speed
        if asteroid.colliderect(ship.ship):
            ship.play_crash_sound()
            game_states.health -= 1
            asteroids.remove(asteroid)
        elif asteroid.y > 650:
            game_states.health -= 1
            asteroids.remove(asteroid)
        else:
            for bullet in ship.bullets[:]:
                if asteroid.colliderect(bullet):
                    game_states.score += 1
                    game_states.level_points += 1
                    asteroids.remove(asteroid)
                    ship.bullets.remove(bullet)
                    break


def draw(screen):
    background.draw()
    for asteroid in asteroids:
        asteroid.draw()
    ship.draw()
    hud.draw(screen)


def on_key_down(key, keys):
    if key == keys.SPACE:
        ship.fire()
