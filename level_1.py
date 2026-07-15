from pgzero.actor import Actor
import game_states

WIDTH = 1200
HEIGHT = 600

GRAVITY = 0.8
JUMP_POWER = -16
MOVE_SPEED = 7

background = Actor("level_1_bg")
background.pos = (WIDTH / 2, HEIGHT / 2)

player = Actor("crab_small")
player.pos = (80, HEIGHT - 60)
player.on_ground = False
player_y_speed = 0

goal = Actor("empty_goal", pos=(1000, 20))

platforms = [
    Actor("platform_counter_small", pos=(200, 500)),
    Actor("platform_counter_small", pos=(400, 400)),
    Actor("platform_counter_small", pos=(200, 250)),
    Actor("platform_counter_small", pos=(500, 250)),
    Actor("platform_counter_small", pos=(650, 180)),
    Actor("platform_counter_small", pos=(750, 300)),
    Actor("platform_counter_small", pos=(950, 150)),
]


def reset():
    global player_y_speed
    player.pos = (80, HEIGHT - 60)
    player_y_speed = 0
    player.on_ground = False
    game_states.is_game_over = False
    game_states.has_won = False


def draw(screen):
    background.draw()
    for p in platforms:
        p.draw()
    player.draw()
    goal.draw()

    if game_states.has_won:
        screen.draw.text(
            "WINNER! Press 'ENTER' for LEVEL SELECT",
            center=(WIDTH / 2, HEIGHT / 2),
            fontsize=60,
            color="lime",
            owidth=2,
            ocolor="black",
        )
    elif game_states.is_game_over:
        screen.draw.text(
            "GAME OVER! Press 'R' to Restart",
            center=(WIDTH / 2, HEIGHT / 2),
            fontsize=60,
            color="red",
            owidth=2,
            ocolor="black",
        )


def update(keyboard):
    global player_y_speed

    if game_states.is_game_over or game_states.has_won:
        return

    if keyboard.left or keyboard.a:
        player.x = player.x - MOVE_SPEED
    if keyboard.right or keyboard.d:
        player.x = player.x + MOVE_SPEED

    if player.left < 0:
        player.left = 0
    if player.right > WIDTH:
        player.right = WIDTH

    player.on_ground = False
    player_y_speed = player_y_speed + GRAVITY
    player.y = player.y + player_y_speed

    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT
        player_y_speed = 0
        player.on_ground = True

    for p in platforms:
        if player.colliderect(p):
            if player_y_speed > 0:
                player.bottom = p.top
                player_y_speed = 0
                player.on_ground = True
            elif player_y_speed < 0:
                player.top = p.bottom
                player_y_speed = 0

    if player.colliderect(goal):
        game_states.has_won = True


def on_key_down(key, keys):
    global player_y_speed

    if (
        key == keys.SPACE
        and player.on_ground
        and not (game_states.is_game_over or game_states.has_won)
    ):
        player_y_speed = JUMP_POWER

    if key == keys.R and (game_states.is_game_over or game_states.has_won):
        reset()

    if key == keys.RETURN and game_states.has_won:
        game_states.game_mode = "LEVEL_SELECT"
        game_states.has_won = False
