from pgzero.actor import Actor
import game_states
import random

WIDTH = 1200
HEIGHT = 600

MOVE_SPEED = 3
POLLUTION_SPEED = 2
SURVIVAL_SECONDS = 10

background = Actor("level_3_bg")
background.pos = (WIDTH / 2, HEIGHT / 2)

player = Actor("crab_small")
player.pos = (80, HEIGHT - 30)

sea_turtle = Actor("turtle")
sea_turtle.pos = (WIDTH - 100, HEIGHT - 90)

pollution_items = []
spawn_timer = 0
timer_frames = SURVIVAL_SECONDS * 60
show_turtle = False


def reset():
    global pollution_items, spawn_timer, timer_frames, show_turtle
    player.pos = (80, HEIGHT - 30)
    pollution_items.clear()
    spawn_timer = 0
    timer_frames = SURVIVAL_SECONDS * 60
    show_turtle = False
    game_states.is_game_over = False
    game_states.has_won = False


def draw(screen):
    background.draw()
    for item in pollution_items:
        item.draw()

    if show_turtle:
        sea_turtle.draw()
        screen.draw.text(
            "FOLLOW THE TURTLE TO SAFETY!",
            (WIDTH / 2 - 250, 50),
            fontsize=40,
            color="lime",
            owidth=1.5,
            ocolor="black",
        )
    else:
        seconds_left = max(0, timer_frames // 60)
        screen.draw.text(
            f"ESCAPE THE POLLUTION: {seconds_left}s",
            (WIDTH / 2 - 250, 50),
            fontsize=50,
            color="orange",
            owidth=2,
            ocolor="black",
        )

    player.draw()

    if game_states.has_won:
        screen.draw.text(
            "YOU ARE SAFE! THE OCEAN IS BEAUTIFUL!",
            center=(WIDTH / 2, HEIGHT / 2),
            fontsize=60,
            color="cyan",
            owidth=2,
            ocolor="black",
        )
        screen.draw.text(
            "Press 'ENTER' for LEVEL SELECT",
            center=(WIDTH / 2, HEIGHT / 2 + 60),
            fontsize=30,
            color="white",
            owidth=1.5,
            ocolor="black",
        )
    elif game_states.is_game_over:
        screen.draw.text(
            "STUCK IN PLASTIC! Press 'R' to Restart",
            center=(WIDTH / 2, HEIGHT / 2),
            fontsize=60,
            color="red",
            owidth=2,
            ocolor="black",
        )


def update(keyboard):
    global spawn_timer, timer_frames, show_turtle, pollution_items

    if game_states.is_game_over or game_states.has_won:
        return

    if timer_frames > 0:
        timer_frames = timer_frames - 1
    else:
        show_turtle = True

    if keyboard.left or keyboard.a:
        player.x = player.x - MOVE_SPEED
    if keyboard.right or keyboard.d:
        player.x = player.x + MOVE_SPEED

    if player.left < 0:
        player.left = 0
    if player.right > WIDTH:
        player.right = WIDTH

    spawn_timer = spawn_timer + 1
    if spawn_timer > 10:
        spawn_timer = 0
        junk = Actor(random.choice(["trash_1", "trash_2", "trash_3", "trash_4"]))
        junk.pos = (random.randint(100, WIDTH - 100), -50)
        pollution_items.append(junk)

    for item in pollution_items:
        item.y = item.y + POLLUTION_SPEED
        if item.colliderect(player):
            game_states.is_game_over = True

    pollution_items = [i for i in pollution_items if i.top < HEIGHT]

    if show_turtle:
        if player.colliderect(sea_turtle):
            game_states.has_won = True


def on_key_down(key, keys):
    if key == keys.R and (game_states.is_game_over or game_states.has_won):
        reset()

    if key == keys.RETURN and game_states.has_won:
        game_states.game_mode = "LEVEL_SELECT"
        game_states.has_won = False
