# What is drawn on top of every flying Level: score, hearts, buttons and the pause screen.
# (The Launch pad draws its own top bar and only borrows draw_pause.)
from pgzero.actor import Actor
from parts import game_states
from parts import controls
from data.level_data import LEVELS

heart = Actor("ui/health")


def draw(screen):
    level = LEVELS[game_states.level_number]
    screen.draw.text(f"Score: {game_states.score}", topleft=(20, 20), fontsize=50, color="yellow", owidth=1.5, ocolor="black")
    screen.draw.text(level["name"], midtop=(400, 15), fontsize=36, color="cyan", owidth=1.5, ocolor="black")
    screen.draw.text(f"{game_states.level_points} / {level['target']}", midtop=(400, 55), fontsize=36, color="white", owidth=1.5, ocolor="black")
    for i in range(game_states.health):
        heart.pos = (760 - i * 50, 40)
        heart.draw()
    controls.draw_buttons()
    draw_pause(screen)


def draw_pause(screen):
    if game_states.paused:
        screen.draw.text("PAUSED", center=(400, 280), fontsize=80, color="orange", owidth=1.5, ocolor="black")
        screen.draw.text("press P or click continue", center=(400, 340), fontsize=36, color="white", owidth=1.5, ocolor="black")
        controls.continue_button.draw()
