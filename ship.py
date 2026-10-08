# The Ship and its footballs (bullets). Every Level uses the same Ship.
from pgzero.actor import Actor
import pygame
import controls

SHIP_Y = 470          # high enough that the buttons at the bottom never cover it
SHIP_SPEED = 9        # pixels per frame
BULLET_SPEED = 10
AUTO_FIRE_EVERY = 30  # frames. The game runs at 60 frames a second, so this is every half second.

ship = Actor("characters/ship", (400, SHIP_Y))
bullets = []
fire_timer = 0


def reset():
    global fire_timer
    ship.pos = (400, SHIP_Y)
    bullets.clear()
    fire_timer = 0


def move(keyboard):
    if (keyboard.left or controls.held == "left") and ship.x > 50:
        ship.x -= SHIP_SPEED
    if (keyboard.right or controls.held == "right") and ship.x < 750:
        ship.x += SHIP_SPEED


def fire():
    bullet = Actor("football")
    bullet.pos = (ship.x, ship.y - 40)
    bullets.append(bullet)


def update_bullets(auto_fire):
    global fire_timer
    if auto_fire:
        fire_timer += 1
        if fire_timer > AUTO_FIRE_EVERY:
            fire()
            fire_timer = 0
    for bullet in bullets[:]:
        bullet.y -= BULLET_SPEED
        if bullet.y < -50:
            bullets.remove(bullet)


def play_crash_sound():
    crash_sound = pygame.mixer.Sound("music/crash.mp3")
    crash_sound.set_volume(0.4)
    crash_sound.play()


def draw():
    ship.draw()
    for bullet in bullets:
        bullet.draw()
