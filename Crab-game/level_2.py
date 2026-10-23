from pgzero.actor import Actor
import game_states
import random

WIDTH = 1200
HEIGHT = 600

MOVE_SPEED = 6
BIRD_SPEED = 2
SURVIVAL_SECONDS = 30

background = Actor("level_2_bg")
background.pos = (WIDTH / 2, HEIGHT / 2)

player = Actor("crab_small")
player.pos = (100, HEIGHT - 30)

sea_wave = Actor("wave")
sea_wave.pos = (WIDTH - 60, HEIGHT - 60)

birds = []
bird_spawn_timer = 0
timer_frames = SURVIVAL_SECONDS * 60
show_goal = False


def draw(screen):
    background.draw()
    player.draw()
    for bird in birds:
        bird.draw()

    if show_goal:
        sea_wave.draw()
        screen.draw.text(
            "THE WAVE IS COMING! GET TO THE WATER!",
            (WIDTH / 2 - 250, 50),
            fontsize=40,
            color="cyan",
            owidth=1.5,
            ocolor="black",
        )
    else:
        seconds_left = max(0, timer_frames // 60)
        screen.draw.text(
            f"THE WAVE COMES IN : {seconds_left}s",
            (WIDTH / 2 - 250, 50),
            fontsize=60,
            color="white",
            owidth=2,
            ocolor="black",
        )

    if game_states.has_won:
        screen.draw.text(
            "WINNER! YOU REACHED THE SEA!",
            center=(WIDTH / 2, HEIGHT / 2),
            fontsize=60,
            color="lime",
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
            "CAUGHT! Press 'R' to Restart",
            center=(WIDTH / 2, HEIGHT / 2),
            fontsize=60,
            color="red",
            owidth=2,
            ocolor="black",
        )


def update(keyboard):
    global bird_spawn_timer, timer_frames, show_goal, birds

    if game_states.is_game_over or game_states.has_won:
        return

    if timer_frames > 0:
        timer_frames = timer_frames - 1
    else:
        show_goal = True

    if keyboard.left or keyboard.a:
        player.x = player.x - MOVE_SPEED
    if keyboard.right or keyboard.d:
        player.x = player.x + MOVE_SPEED

    if player.left < 0:
        player.left = 0
    if player.right > WIDTH:
        player.right = WIDTH

    bird_spawn_timer = bird_spawn_timer + 1
    if bird_spawn_timer > 20:
        bird_spawn_timer = 0
        new_bird = Actor("bird")
        new_bird.pos = (random.randint(0, WIDTH), -50)
        birds.append(new_bird)

    for bird in birds:
        bird.y = bird.y + BIRD_SPEED
        if bird.colliderect(player):
            game_states.is_game_over = True

    birds_on_screen = []
    for bird in birds:
        if bird.top < HEIGHT:
            birds_on_screen.append(bird)

    birds = birds_on_screen

    if show_goal:
        if player.colliderect(sea_wave):
            game_states.has_won = True


def on_key_down(key, keys):
    if key == keys.R and (game_states.is_game_over or game_states.has_won):
        reset()

    if key == keys.RETURN and game_states.has_won:
        game_states.game_mode = "LEVEL_SELECT"
        game_states.has_won = False
        game_states.is_game_over = False


def reset():
    global birds, bird_spawn_timer, timer_frames, show_goal
    player.pos = (100, HEIGHT - 30)
    birds.clear()
    bird_spawn_timer = 0
    timer_frames = SURVIVAL_SECONDS * 60
    show_goal = False
    game_states.is_game_over = False
    game_states.has_won = False
