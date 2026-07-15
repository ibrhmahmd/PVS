from pgzero.actor import Actor
import pygame
import game_states
import random

WIDTH = 1200
HEIGHT = 600

background = Actor("start-screen-background")
background.pos = (WIDTH / 2, HEIGHT / 2)

decorations = [
    Actor("clown_fish", (180, 150)),
    Actor("blue_fish", (950, 220)),
    Actor("pink_fish", (450, 100)),
    Actor("green_fish", (200, 400)),
    Actor("orange_fish", (800, 80)),
    Actor("sea_star_small", (130, 550)),
    Actor("sea_star_small", (1050, 520)),
    Actor("closed_clam_small", (350, 570)),
    Actor("opened_clam_small", (800, 550)),
    Actor("half_clam_small", (600, 540)),
]

for i, item in enumerate(decorations):
    if "fish" in item.image:
        item.speed = random.choice([-2, 2])
    else:
        item.speed = 0

start_button = Actor("start_btn")
start_button.pos = (WIDTH / 2, HEIGHT - 200)

logo = Actor("logo")
logo.pos = (WIDTH / 2, HEIGHT - 400)

crab = Actor("crab_medium")
crab.pos = (WIDTH / 2, HEIGHT - 60)


def draw(screen):
    background.draw()
    for item in decorations:
        item.draw()
    start_button.draw()
    logo.draw()
    crab.draw()


def update():
    for item in decorations:
        if item.speed != 0:
            item.x += item.speed
            if item.x > WIDTH + 50:
                item.x = -50
            elif item.x < -50:
                item.x = WIDTH + 50

    if start_button.collidepoint(pygame.mouse.get_pos()):
        start_button.image = "start_btn_hover"
    else:
        start_button.image = "start_btn"


def on_mouse_down(pos):
    if start_button.collidepoint(pos):
        game_states.game_mode = "LEVEL_SELECT"
