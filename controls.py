# The on-screen buttons (for mouse or touch). The keyboard works too.
from pgzero.actor import Actor
import game_states

left_button = Actor("buttons/left", (50, 550))
right_button = Actor("buttons/right", (140, 550))
pause_button = Actor("buttons/pause", (750, 550))
continue_button = Actor("buttons/continue", (400, 400))

# Which move button the mouse is holding down right now: "left", "right" or None
held = None


def on_mouse_down(pos):
    global held
    if game_states.paused:
        if continue_button.collidepoint(pos):
            game_states.paused = False
        return
    if pause_button.collidepoint(pos):
        game_states.paused = True
    elif left_button.collidepoint(pos):
        held = "left"
    elif right_button.collidepoint(pos):
        held = "right"


def on_mouse_up():
    global held
    held = None


def draw_buttons():
    left_button.draw()
    right_button.draw()
    pause_button.draw()
