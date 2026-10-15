# The Title screen: the very first screen, before any Level. Press Space (or click) to start.
from pgzero.actor import Actor
from parts import game_states
from data.level_data import TITLE_STORY

background = Actor("backgrounds/space_background", (400, 300))
logo = Actor("ui/logo", (400, 95))
hero = Actor("characters/hero", (400, 300))


def go():
    # Start the Journey at Level 1, the Launch pad.
    game_states.level_number = 0
    game_states.mode = "NEXT_LEVEL"


def draw(screen):
    background.draw()
    logo.draw()
    hero.draw()
    screen.draw.text(" ".join(TITLE_STORY), midtop=(400, 415), width=700, fontsize=30, color="cyan", align="center", owidth=1.5, ocolor="black")
    if game_states.high_score > 0:
        screen.draw.text(f"High Score: {game_states.high_score}", center=(400, 505), fontsize=36, color="yellow", owidth=1.5, ocolor="black")
    screen.draw.text("Press Space to start", center=(400, 560), fontsize=50, color="white", owidth=1.5, ocolor="black")
