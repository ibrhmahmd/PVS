# Shown when a Level is cleared: what happens next in the mission, and one fact about the place we just passed.
from pgzero.actor import Actor
from pygame import Rect
from parts import game_states
from data.level_data import LEVELS

hero = Actor("characters/hero", (140, 330))


def go():
    # Space or a click: on to the next Level.
    game_states.level_number += 1
    game_states.mode = "NEXT_LEVEL"


def draw(screen, background):
    background.draw()
    screen.draw.filled_rect(Rect(40, 60, 720, 480), (10, 10, 40))
    screen.draw.rect(Rect(40, 60, 720, 480), "cyan")
    screen.draw.text("Level cleared!", center=(400, 110), fontsize=60, color="yellow", owidth=1.5, ocolor="black")
    hero.draw()
    level = LEVELS[game_states.level_number]
    screen.draw.text(" ".join(level["story"]), topleft=(260, 160), width=470, fontsize=30, color="cyan", owidth=1.5, ocolor="black")
    screen.draw.text(" ".join(level["fact"]), topleft=(260, 290), width=470, fontsize=30, color="white", owidth=1.5, ocolor="black")
    screen.draw.text("Press Space to continue", center=(400, 505), fontsize=36, color="white", owidth=1.5, ocolor="black")
