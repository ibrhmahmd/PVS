from pgzero.actor import Actor
import game_states

WIDTH = 1200
HEIGHT = 600

GRAVITY = 0.5
JUMP_POWER = -12
MOVE_SPEED = 6
FISH_SPEED = 7

Ground_line = HEIGHT - 20
background = Actor("level_5_bg")
background.pos = (WIDTH / 2, HEIGHT / 2)

SURVIVAL_SECONDS = 45
timer_frames = SURVIVAL_SECONDS * 60

player = Actor("crab_small")
player.pos = (150, Ground_line)
player.on_ground = False
player_y_speed = 0

patrol_fish = Actor("evil_red_fish_right")
patrol_fish.pos = (WIDTH / 2, 550)
fish_direction = 1


def draw(screen):
    background.draw()
    patrol_fish.draw()
    player.draw()

    screen.draw.text(
        "SURVIVE THE PATROLLING FISH!",
        (WIDTH / 2 - 250, 20),
        fontsize=30,
        color="cyan",
        owidth=1.5,
        ocolor="black",
    )

    seconds_left = max(0, timer_frames // 60)
    screen.draw.text(
        f"TIME TO ESCAPE: {seconds_left}s",
        (WIDTH / 2 - 150, 70),
        fontsize=40,
        color="orange",
        owidth=1.5,
        ocolor="black",
    )

    if game_states.has_won:
        screen.draw.text(
            "YOU DODGED IT! REACH THE REEF!",
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
            "OOPS! Press 'R' to Restart",
            center=(WIDTH / 2, HEIGHT / 2),
            fontsize=60,
            color="red",
            owidth=2,
            ocolor="black",
        )


def update(keyboard):
    global player_y_speed, fish_direction, timer_frames

    if game_states.is_game_over or game_states.has_won:
        return

    timer_frames -= 1
    if timer_frames <= 0 and not game_states.is_game_over:
        game_states.has_won = True

    if keyboard.left or keyboard.a:
        player.x = player.x - MOVE_SPEED
    if keyboard.right or keyboard.d:
        player.x = player.x + MOVE_SPEED

    if timer_frames <= 0:
        game_states.has_won = True

    if player.left < 0:
        player.left = 0
    if player.right > WIDTH:
        player.right = WIDTH

    player.on_ground = False
    player_y_speed = player_y_speed + GRAVITY
    player.y = player.y + player_y_speed

    if player.bottom >= Ground_line:
        player.bottom = Ground_line
        player_y_speed = 0
        player.on_ground = True

    patrol_fish.x = patrol_fish.x + (FISH_SPEED * fish_direction)

    if patrol_fish.right > WIDTH:
        fish_direction = -1
        patrol_fish.image = "evil_red_fish_left"
    elif patrol_fish.left < 0:
        fish_direction = 1
        patrol_fish.image = "evil_red_fish_right"

    if player.colliderect(patrol_fish):
        game_states.is_game_over = True


def on_key_down(key, keys):
    global player_y_speed

    if key == keys.SPACE and player.on_ground:
        player_y_speed = JUMP_POWER

    if key == keys.R and (game_states.is_game_over or game_states.has_won):
        reset()

    if key == keys.RETURN and game_states.has_won:
        game_states.game_mode = "LEVEL_SELECT"
        game_states.has_won = False
        game_states.is_game_over = False


def reset():
    global player_y_speed, fish_direction, timer_frames
    player.pos = (150, Ground_line)
    player_y_speed = 0
    player.on_ground = False
    patrol_fish.pos = (WIDTH / 2, 550)
    fish_direction = 1
    timer_frames = SURVIVAL_SECONDS * 60
    game_states.is_game_over = False
    game_states.has_won = False
