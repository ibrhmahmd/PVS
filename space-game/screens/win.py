# The last screen: the Hero reached Jupiter!
from pgzero.actor import Actor
from pygame import Rect
from parts import game_states
from data.level_data import WIN_STORY, WIN_FACT

background = Actor("backgrounds/jupiter", (400, 300))
hero = Actor("characters/hero", (140, 330))


def start():
    game_states.mode = "WIN"
    if game_states.score > game_states.high_score:
        game_states.high_score = game_states.score


def go():
    # R or a click: back to the Title screen, ready to fly the whole Journey again.
    game_states.score = 0
    game_states.level_number = 0
    game_states.mode = "TITLE"


def draw(screen):
    background.draw()
    screen.draw.text("YOU REACHED JUPITER!", center=(400, 60), fontsize=70, color="yellow", owidth=1.5, ocolor="black")
    hero.draw()
    screen.draw.filled_rect(Rect(245, 115, 510, 230), (10, 10, 40))  # dark panel so the words are easy to read
    screen.draw.text(" ".join(WIN_STORY), topleft=(260, 130), width=470, fontsize=32, color="cyan", owidth=1.5, ocolor="black")
    screen.draw.text(" ".join(WIN_FACT), topleft=(260, 230), width=470, fontsize=30, color="white", owidth=1.5, ocolor="black")
    screen.draw.text(f"Score: {game_states.score}", center=(400, 430), fontsize=50, color="white", owidth=1.5, ocolor="black")
    screen.draw.text(f"High Score: {game_states.high_score}", center=(400, 480), fontsize=40, color="cyan", owidth=1.5, ocolor="black")
    screen.draw.text("Press R to fly again", center=(400, 550), fontsize=50, color="white", owidth=1.5, ocolor="black")
