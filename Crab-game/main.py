from pgzero.actor import Actor
from pgzero.constants import keys
import pgzrun
import game_states
import start_screen
import level_1
import level_2
import level_3
import level_4
import level_5
import level_6
import level_select

WIDTH = 1200
HEIGHT = 600
TITLE = "Crab Game"
LEVEL_MODES = ["LEVEL1", "LEVEL2", "LEVEL3", "LEVEL4", "LEVEL5", "LEVEL6"]

 
mute_button = Actor("music_on")
mute_button.pos = (WIDTH - 50, 50)


def draw():
    screen.clear()
    if game_states.game_mode == "START_SCREEN":
        start_screen.draw(screen)
    elif game_states.game_mode == "LEVEL_SELECT":
        level_select.draw(screen)
    elif game_states.game_mode == "LEVEL1":
        level_1.draw(screen)
    elif game_states.game_mode == "LEVEL2":
        level_2.draw(screen)
    elif game_states.game_mode == "LEVEL3":
        level_3.draw(screen)
    elif game_states.game_mode == "LEVEL4":
        level_4.draw(screen)
    elif game_states.game_mode == "LEVEL5":
        level_5.draw(screen)
    elif game_states.game_mode == "LEVEL6":
        level_6.draw(screen)

    if game_states.game_mode in LEVEL_MODES:
        screen.draw.text("ESC: chapters", topleft=(10, 10), fontsize=24, color="white", owidth=1.5, ocolor="black")

    mute_button.draw()


def update():
    if game_states.game_mode == "START_SCREEN":
        start_screen.update()
    elif game_states.game_mode == "LEVEL_SELECT":
        level_select.update()
    elif game_states.game_mode == "LEVEL1":
        level_1.update(keyboard)
    elif game_states.game_mode == "LEVEL2":
        level_2.update(keyboard)
    elif game_states.game_mode == "LEVEL3":
        level_3.update(keyboard)
    elif game_states.game_mode == "LEVEL4":
        level_4.update(keyboard)
    elif game_states.game_mode == "LEVEL5":
        level_5.update(keyboard)
    elif game_states.game_mode == "LEVEL6":
        level_6.update(keyboard)


def on_mouse_down(pos):
    if mute_button.collidepoint(pos):
        if game_states.is_music_on:
            music.set_volume(0)
            mute_button.image = "music_off"
            game_states.is_music_on = False
        else:
            music.set_volume(1)
            mute_button.image = "music_on"
            game_states.is_music_on = True
        return

    if game_states.game_mode == "START_SCREEN":
        start_screen.on_mouse_down(pos)
    elif game_states.game_mode == "LEVEL_SELECT":
        level_select.on_mouse_down(pos)


def on_key_down(key):
    # ESC always gets you out: from a level to the chapters, from the chapters to the start.
    if key == keys.ESCAPE and game_states.game_mode in LEVEL_MODES:
        game_states.is_game_over = False
        game_states.has_won = False
        game_states.game_mode = "LEVEL_SELECT"
        return
    if key == keys.ESCAPE and game_states.game_mode == "LEVEL_SELECT":
        game_states.game_mode = "START_SCREEN"
        return

    if game_states.game_mode == "LEVEL1":
        level_1.on_key_down(key, keys)
    elif game_states.game_mode == "LEVEL2":
        level_2.on_key_down(key, keys)
    elif game_states.game_mode == "LEVEL3":
        level_3.on_key_down(key, keys)
    elif game_states.game_mode == "LEVEL4":
        level_4.on_key_down(key, keys)
    elif game_states.game_mode == "LEVEL5":
        level_5.on_key_down(key, keys)
    elif game_states.game_mode == "LEVEL6":
        level_6.on_key_down(key, keys)


try:
    music.play("background_music")
except:
    pass

pgzrun.go()
