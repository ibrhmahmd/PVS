from pgzero.actor import Actor
import game_states

WIDTH = 1200
HEIGHT = 600

GRAVITY = 0.5
JUMP_POWER = -12
MOVE_SPEED = 5

background = Actor("level_6_bg")
background.pos = (WIDTH / 2, HEIGHT / 2)

player = Actor("crab_small")
player.pos = (150, HEIGHT - 30)
player.on_ground = False
player_y_speed = 0

family = [
    Actor("crab_medium", pos=(WIDTH - 200, HEIGHT - 60)),
    Actor("crab_medium", pos=(WIDTH - 150, HEIGHT - 80)),
]


def reset():
    global player_y_speed
    player.pos = (150, HEIGHT - 30)
    player_y_speed = 0
    player.on_ground = False
    game_states.is_game_over = False
    game_states.has_won = False


def draw(screen):
    background.draw()
    for member in family:
        member.draw()
    player.draw()

    screen.draw.text(
        "YOU MADE IT! THE PROTECTED SANCTUARY.",
        (WIDTH / 2 - 350, 50),
        fontsize=40,
        color="lime",
        owidth=2,
        ocolor="black",
    )
    screen.draw.text(
        "RUN TOWARDS FAMILY",
        (WIDTH / 2 - 150, 110),
        fontsize=30,
        color="white",
        owidth=1.5,
        ocolor="black",
    )

    if game_states.has_won:
        screen.draw.text(
            "REUNITED! YOU ARE HOME.",
            center=(WIDTH / 2, HEIGHT / 2),
            fontsize=60,
            color="gold",
            owidth=2,
            ocolor="black",
        )
        screen.draw.text(
            "THE END - Press 'ENTER' for START SCREEN",
            center=(WIDTH / 2, HEIGHT / 2 + 60),
            fontsize=30,
            color="cyan",
            owidth=1.5,
            ocolor="black",
        )


def update(keyboard):
    global player_y_speed

    if game_states.has_won:
        return

    if keyboard.left or keyboard.a:
        player.x -= MOVE_SPEED
    if keyboard.right or keyboard.d:
        player.x += MOVE_SPEED

    if player.left < 0:
        player.left = 0
    if player.right > WIDTH:
        player.right = WIDTH

    # Jumping Physics
    player.on_ground = False
    player_y_speed += GRAVITY
    player.y += player_y_speed

    if player.bottom >= HEIGHT - 20:
        player.bottom = HEIGHT - 20
        player_y_speed = 0
        player.on_ground = True

    # Win condition
    for member in family:
        if player.colliderect(member):
            game_states.has_won = True


def on_key_down(key, keys):
    global player_y_speed

    if key == keys.SPACE and player.on_ground:
        player_y_speed = JUMP_POWER

    if key == keys.RETURN and game_states.has_won:
        game_states.game_mode = "START_SCREEN"
        game_states.has_won = False
        game_states.is_game_over = False
