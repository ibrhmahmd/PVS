from pgzero.actor import Actor
import pygame
import game_states
import level_1
import level_2
import level_3
import level_4
import level_5
import level_6

WIDTH = 1200
HEIGHT = 600

background = Actor("start-screen-background")
background.pos = (WIDTH / 2, HEIGHT / 2)

decorations = [
    Actor("sea_star_small", (80, 80)),
    Actor("sea_star_small", (WIDTH - 80, HEIGHT - 80)),
    Actor("closed_clam_small", (WIDTH - 150, 100)),
    Actor("opened_clam_small", (150, HEIGHT - 100)),
    Actor("blue_fish", (100, 250)),
    Actor("pink_fish", (1100, 300)),
    Actor("orange_fish", (500, 120)),
    Actor("green_fish", (750, 550)),
    Actor("clown_fish", (420, 350)),
    Actor("bubble_fish_small", (780, 350)),
    Actor("gold_fish_small", (50, 450)),
    Actor("half_clam_small", (WIDTH / 2, HEIGHT - 40)),
]

COL1, COL2, COL3 = 250, 600, 950
ROW1, ROW2 = 250, 450

level1_btn = Actor("start_btn", (COL1, ROW1))
level2_btn = Actor("start_btn", (COL2, ROW1))
level3_btn = Actor("start_btn", (COL3, ROW1))
level4_btn = Actor("start_btn", (COL1, ROW2))

level5_btn = Actor("start_btn", (COL2, ROW2))
level6_btn = Actor("start_btn", (COL3, ROW2))

buttons = [level1_btn, level2_btn, level3_btn, level4_btn, level5_btn, level6_btn]
labels = [
    "1. KITCHEN ESCAPE 🪟",
    "2. BEACH RUN 🦅",
    "3. SEA FLOOR DODGING 🐢",
    "4. SHRIMP HELP 🦐",
    "5. PREDATOR CHASE 🦈",
    "6. HOME SWEET HOME 🪸",
]


def draw(screen):
    background.draw()
    for dec in decorations:
        dec.draw()

    screen.draw.text(
        "CHOOSE YOUR CHAPTER",
        center=(WIDTH / 2, 70),
        fontsize=70,
        color="yellow",
        owidth=2,
        ocolor="black",
    )

    for i in range(6):
        buttons[i].draw()
        screen.draw.text(
            labels[i],
            center=buttons[i].pos,
            fontsize=25,
            color="white",
            owidth=1.5,
            ocolor="black",
        )


def update():
    mouse_pos = pygame.mouse.get_pos()
    for btn in buttons:
        if btn.collidepoint(mouse_pos):
            btn.image = "start_btn_hover"
        else:
            btn.image = "start_btn"


def on_mouse_down(pos):
    if level1_btn.collidepoint(pos):
        level_1.reset()
        game_states.game_mode = "LEVEL1"
    elif level2_btn.collidepoint(pos):
        level_2.reset()
        game_states.game_mode = "LEVEL2"
    elif level3_btn.collidepoint(pos):
        level_3.reset()
        game_states.game_mode = "LEVEL3"
    elif level4_btn.collidepoint(pos):
        level_4.reset()
        game_states.game_mode = "LEVEL4"
    elif level5_btn.collidepoint(pos):
        level_5.reset()
        game_states.game_mode = "LEVEL5"
    elif level6_btn.collidepoint(pos):
        level_6.reset()
        game_states.game_mode = "LEVEL6"
