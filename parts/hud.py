# What is drawn on top of every Level: score, hearts, buttons and the pause screen.
from pgzero.actor import Actor
from parts import game_states
from parts import controls
from data.level_data import LEVELS

heart = Actor("health")


def draw(screen):
    level = LEVELS[game_states.level_number]
    screen.draw.text(f"Score: {game_states.score}", topleft=(20, 20), fontsize=50, color="yellow")
    screen.draw.text(level["name"], midtop=(400, 15), fontsize=36, color="cyan")
    screen.draw.text(f"{game_states.level_points} / {level['target']}", midtop=(400, 55), fontsize=36, color="white")
    for i in range(game_states.health):
        heart.pos = (760 - i * 50, 40)
        heart.draw()
    controls.draw_buttons()
    if game_states.paused:
        screen.draw.text("PAUSED", center=(400, 280), fontsize=80, color="orange")
        screen.draw.text("press P or click continue", center=(400, 340), fontsize=36, color="white")
        controls.continue_button.draw()
