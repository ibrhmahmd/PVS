# Shown when all the hearts are gone. It teaches a random fact about the solar system.
import random
import pygame
from pygame import Rect
from parts import game_states
from data.game_data import space_info_list

planet_info = None
planet_image = None


def start():
    global planet_info, planet_image
    game_states.mode = "GAME_OVER"
    if game_states.score > game_states.high_score:
        game_states.high_score = game_states.score
    planet_info = random.choice(space_info_list)
    planet_image = pygame.image.load(planet_info["image"])


def go():
    # R or a click: try this same Level again, with the score from when it began.
    game_states.score = game_states.level_start_score
    game_states.mode = "RETRY_LEVEL"


def draw(screen, background):
    background.draw()
    image_rect = planet_image.get_rect()
    image_rect.center = (400, 150)
    screen.surface.blit(planet_image, image_rect)
    screen.draw.filled_rect(Rect(40, 270, 720, 320), (10, 10, 40))  # dark panel so the words are easy to read
    screen.draw.text(" ".join(planet_info["text"]), midtop=(400, 280), width=700, fontsize=40,
                     color="white", align="center", shadow=(1, 1), scolor="black")
    screen.draw.text("GAME OVER", center=(400, 480), fontsize=120, color="red")
    screen.draw.text("Press R to try this Level again", center=(400, 550), fontsize=50, color="white")
