# Space X: Journey to Jupiter.
# This file only holds the three Pygame Zero hooks (draw, update, on_key_down) and the mouse hooks.
# Screens are in screens/, Levels in levels/, shared pieces in parts/, facts and numbers in data/.
# game_states.mode (in parts/game_states.py) says which screen is showing.
import os
import sys
import pygame
import pgzrun
from pgzero.keyboard import keys
from parts import game_states
from parts import controls
from screens import intro
from screens import fact_card
from screens import game_over
from screens import win
from levels import earth
from levels import belt
from levels import europa
from data.level_data import LEVELS

# Always look for images/ and music/ next to this file, even when started from another folder
# or from a PyInstaller build (which unpacks its files into sys._MEIPASS).
GAME_FOLDER = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
os.chdir(GAME_FOLDER)

WIDTH = 800
HEIGHT = 600

# Level 1, 2 and 3 in the same order as LEVELS in level_data.py
LEVEL_FILES = [earth, belt, europa]


def start_level():
    # Called when a Level begins (the first time, or after a Fact card).
    game_states.mode = "PLAYING"
    game_states.level_points = 0
    game_states.level_start_score = game_states.score
    game_states.health = 3
    LEVEL_FILES[game_states.level_number].start()


def current_level():
    return LEVEL_FILES[game_states.level_number]


def draw():
    mode = game_states.mode
    if mode == "INTRO":
        intro.draw(screen)
    elif mode == "PLAYING":
        current_level().draw(screen)
    elif mode == "FACT_CARD":
        fact_card.draw(screen, current_level().background)
    elif mode == "GAME_OVER":
        game_over.draw(screen, current_level().background)
    elif mode == "WIN":
        win.draw(screen)


def update(keyboard):
    mode = game_states.mode

    # Music plays only while we are really playing.
    if mode == "PLAYING" and not game_states.paused:
        if not music.is_playing("music.mp3"):
            music.play("music.mp3")
            music.set_volume(0.9)
    elif music.is_playing("music.mp3"):
        music.stop()

    if mode == "INTRO":
        intro.update()
    elif mode == "PLAYING" and not game_states.paused:
        current_level().update(keyboard)
        if game_states.health <= 0:
            game_over.start()
        elif game_states.level_points >= LEVELS[game_states.level_number]["target"]:
            game_states.mode = "FACT_CARD"

    # screens/intro.py, fact_card.py and game_over.py ask for a new Level by setting these modes.
    if game_states.mode == "NEXT_LEVEL":
        if game_states.level_number >= len(LEVEL_FILES):
            win.start()
        else:
            start_level()
    elif game_states.mode == "RETRY_LEVEL":
        start_level()


def go_to_next_screen():
    # What Space (or a click) does on every screen that is not a Level.
    mode = game_states.mode
    if mode == "INTRO":
        intro.go()
    elif mode == "FACT_CARD":
        fact_card.go()
    elif mode == "GAME_OVER":
        game_over.go()
    elif mode == "WIN":
        win.go()


def on_key_down(key):
    mode = game_states.mode

    if key == keys.F:
        pygame.display.toggle_fullscreen()

    if mode == "PLAYING":
        if key == keys.P:
            game_states.paused = not game_states.paused
        elif not game_states.paused:
            current_level().on_key_down(key, keys)
    elif mode in ("INTRO", "FACT_CARD") and key == keys.SPACE:
        go_to_next_screen()
    elif mode in ("GAME_OVER", "WIN") and key == keys.R:
        go_to_next_screen()


def on_mouse_down(pos):
    if game_states.mode == "PLAYING":
        controls.on_mouse_down(pos)
    else:
        go_to_next_screen()


def on_mouse_up():
    controls.on_mouse_up()


pgzrun.go()
