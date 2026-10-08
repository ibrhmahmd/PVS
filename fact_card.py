# Shown when a Level is cleared. It teaches one thing about the place we just passed.
from pgzero.actor import Actor
from pygame import Rect
import game_states
from level_data import LEVELS

hero = Actor("characters/hero", (140, 330))


def go():
    # Space or a click: on to the next Level.
    game_states.level_number += 1
    game_states.mode = "NEXT_LEVEL"


def draw(screen, background):
    background.draw()
    screen.draw.filled_rect(Rect(40, 60, 720, 480), (10, 10, 40))
    screen.draw.rect(Rect(40, 60, 720, 480), "cyan")
    screen.draw.text("Level cleared!", center=(400, 110), fontsize=60, color="yellow")
    hero.draw()
    fact = LEVELS[game_states.level_number]["fact"]
    screen.draw.text(" ".join(fact), topleft=(260, 170), width=470, fontsize=34, color="white")
    screen.draw.text("Press Space to continue", center=(400, 505), fontsize=36, color="white")
