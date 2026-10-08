from pgzero.actor import Actor
import game_states

WIDTH = 1200
HEIGHT = 600

GRAVITY = 0.5
JUMP_POWER = -12
MOVE_SPEED = 8
Ground_line = HEIGHT - 10
SURVIVAL_SECONDS = 60
timer_frames = SURVIVAL_SECONDS * 60

background = Actor("level_4_bg")
background.pos = (WIDTH / 2, HEIGHT / 2)

shrimp_player = Actor("shrimp")
shrimp_player.pos = (80, HEIGHT - 60)
shrimp_player.on_ground = False
shrimp_y_speed = 0

crab_npc = Actor("crab_small")
crab_npc.pos = (WIDTH - 100, HEIGHT - 60)

platforms = [
    Actor("empty_goal", pos=(50, 425)),
    Actor("empty_goal", pos=(130, 425)),
    Actor("empty_goal", pos=(300, 435)),
    Actor("empty_goal", pos=(150, 255)),
    Actor("empty_goal", pos=(350, 265)),
    Actor("empty_goal", pos=(440, 350)),
    Actor("empty_goal", pos=(50, 125)),
    Actor("empty_goal", pos=(100, 125)),
    Actor("empty_goal", pos=(270, 155)),
    Actor("empty_goal", pos=(880, 495)),
    Actor("empty_goal", pos=(1070, 495)),
    Actor("empty_goal", pos=(1150, 495)),
    Actor("empty_goal", pos=(950, 400)),
    Actor("empty_goal", pos=(1010, 400)),
    Actor("empty_goal", pos=(695, 385)),
    Actor("empty_goal", pos=(910, 310)),
    Actor("empty_goal", pos=(1080, 295)),
    Actor("empty_goal", pos=(1150, 295)),
    Actor("empty_goal", pos=(720, 235)),
    Actor("empty_goal", pos=(765, 235)),
    Actor("empty_goal", pos=(990, 180)),
    Actor("empty_goal", pos=(1125, 150)),
    Actor("empty_goal", pos=(825, 105)),
]

food_items = [
    Actor("crab_food_algae", pos=(50, 395)),
    Actor("crab_food_algae", pos=(300, 405)),
    Actor("crab_food_algae", pos=(150, 225)),
    Actor("crab_food_algae", pos=(350, 235)),
    Actor("crab_food_algae", pos=(50, 95)),
    Actor("crab_food_algae", pos=(270, 125)),
    Actor("crab_food_algae", pos=(880, 465)),
    Actor("crab_food_algae", pos=(1070, 465)),
    Actor("crab_food_algae", pos=(950, 370)),
    Actor("crab_food_algae", pos=(695, 355)),
    Actor("crab_food_algae", pos=(910, 280)),
    Actor("crab_food_algae", pos=(1080, 265)),
    Actor("crab_food_algae", pos=(720, 205)),
    Actor("crab_food_algae", pos=(990, 150)),
    Actor("crab_food_algae", pos=(1125, 120)),
    Actor("crab_food_algae", pos=(825, 75)),
    Actor("crab_food_algae", pos=(445, 345)),
]


def draw(screen):
    background.draw()
    for platform in platforms:
        platform.draw()
    for food in food_items:
        food.draw()
    crab_npc.draw()
    shrimp_player.draw()

    screen.draw.text(
        f"FOOD REMAINING: {len(food_items)}",
        (50, 50),
        fontsize=30,
        color="orange",
        owidth=1.5,
        ocolor="black",
    )
    screen.draw.text(
        "HELP THE EXHAUSTED CRAB!",
        (WIDTH / 2 - 150, 20),
        fontsize=30,
        color="white",
        owidth=1.5,
        ocolor="black",
    )

    seconds_left = max(0, timer_frames // 60)
    screen.draw.text(
        f"TIME LEFT: {seconds_left}s",
        (WIDTH - 250, 50),
        fontsize=30,
        color="white",
        owidth=1.5,
        ocolor="black",
    )

    if game_states.has_won:
        screen.draw.text(
            "CRAB REGAINED STRENGTH!",
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
            "GAME OVER! Press 'R' to Restart",
            center=(WIDTH / 2, HEIGHT / 2),
            fontsize=60,
            color="red",
            owidth=2,
            ocolor="black",
        )


def update(keyboard):
    global shrimp_y_speed, timer_frames

    if game_states.is_game_over or game_states.has_won:
        return

    if timer_frames > 0:
        timer_frames -= 1
    else:
        game_states.is_game_over = True

    if keyboard.left or keyboard.a:
        shrimp_player.x = shrimp_player.x - MOVE_SPEED
    if keyboard.right or keyboard.d:
        shrimp_player.x = shrimp_player.x + MOVE_SPEED

    if shrimp_player.left < 0:
        shrimp_player.left = 0
    if shrimp_player.right > WIDTH:
        shrimp_player.right = WIDTH

    shrimp_player.on_ground = False
    shrimp_y_speed = shrimp_y_speed + GRAVITY
    shrimp_player.y = shrimp_player.y + shrimp_y_speed

    if shrimp_player.bottom >= Ground_line:
        shrimp_player.bottom = Ground_line
        shrimp_y_speed = 0
        shrimp_player.on_ground = True

    for platform in platforms:
        if shrimp_player.colliderect(platform):
            if shrimp_y_speed > 0:
                shrimp_player.bottom = platform.top
                shrimp_y_speed = 0
                shrimp_player.on_ground = True
            elif shrimp_y_speed < 0:
                shrimp_player.top = platform.bottom
                shrimp_y_speed = 0

    for food in food_items:
        if shrimp_player.colliderect(food):
            food_items.remove(food)
            break

    if len(food_items) == 0:
        game_states.has_won = True


def on_key_down(key, keys):
    global shrimp_y_speed

    if key == keys.SPACE and shrimp_player.on_ground:
        shrimp_y_speed = JUMP_POWER

    if key == keys.R and (game_states.is_game_over or game_states.has_won):
        reset()

    if key == keys.RETURN and game_states.has_won:
        game_states.game_mode = "LEVEL_SELECT"
        game_states.has_won = False


def reset():
    global shrimp_y_speed, food_items, timer_frames
    shrimp_player.pos = (80, HEIGHT - 60)
    shrimp_y_speed = 0
    shrimp_player.on_ground = False
    timer_frames = SURVIVAL_SECONDS * 60

    food_items = [
        Actor("crab_food_algae", pos=(50, 395)),
        Actor("crab_food_algae", pos=(300, 405)),
        Actor("crab_food_algae", pos=(150, 225)),
        Actor("crab_food_algae", pos=(350, 235)),
        Actor("crab_food_algae", pos=(50, 95)),
        Actor("crab_food_algae", pos=(270, 125)),
        Actor("crab_food_algae", pos=(880, 465)),
        Actor("crab_food_algae", pos=(1070, 465)),
        Actor("crab_food_algae", pos=(950, 370)),
        Actor("crab_food_algae", pos=(695, 355)),
        Actor("crab_food_algae", pos=(910, 280)),
        Actor("crab_food_algae", pos=(1080, 265)),
        Actor("crab_food_algae", pos=(720, 205)),
        Actor("crab_food_algae", pos=(990, 150)),
        Actor("crab_food_algae", pos=(1125, 120)),
        Actor("crab_food_algae", pos=(825, 75)),
        Actor("crab_food_algae", pos=(445, 345)),
    ]

    game_states.is_game_over = False
    game_states.has_won = False
