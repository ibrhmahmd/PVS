# The last screen: the Hero reached Jupiter!
from pgzero.actor import Actor
import game_states
from level_data import WIN_FACT

background = Actor("backgrounds/jupiter", (400, 300))
hero = Actor("characters/hero", (140, 330))


def start():
    game_states.mode = "WIN"
    if game_states.score > game_states.high_score:
        game_states.high_score = game_states.score


def go():
    # R or a click: fly the whole Journey again from Earth.
    game_states.score = 0
    game_states.level_number = 0
    game_states.mode = "INTRO"


def draw(screen):
    background.draw()
    screen.draw.text("YOU REACHED JUPITER!", center=(400, 60), fontsize=70, color="yellow", shadow=(2, 2), scolor="black")
    hero.draw()
    screen.draw.text(" ".join(WIN_FACT), topleft=(260, 150), width=470, fontsize=34, color="white", shadow=(1, 1), scolor="black")
    screen.draw.text(f"Score: {game_states.score}", center=(400, 430), fontsize=50, color="white", shadow=(1, 1), scolor="black")
    screen.draw.text(f"High Score: {game_states.high_score}", center=(400, 480), fontsize=40, color="cyan", shadow=(1, 1), scolor="black")
    screen.draw.text("Press R to fly again", center=(400, 550), fontsize=50, color="white", shadow=(1, 1), scolor="black")
