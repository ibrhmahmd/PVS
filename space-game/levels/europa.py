# Level 4: Europa. Europa's geysers blast ice into space. Shoot the ice chunks.
# Each chunk needs TWO hits: the first one cracks it.
# When enough ice is broken, the ice stops and the Ship scans for the hidden ocean.
import random
from pgzero.actor import Actor
from pygame import Rect
from parts import game_states
from parts import ship
from parts import hud
from data.level_data import LEVELS

CHUNK_SPEED = 2.5      # slower than asteroids, because chunks are tougher
SPAWN_EVERY = 80       # frames between ice chunks
SCAN_FRAMES = 180      # the Scan takes 3 seconds (60 frames a second)
FOUND_FRAMES = 60      # then "Ocean found!" stays for 1 second

background = Actor("backgrounds/europa", (400, 300))
chunks = []
timer = 0
scanning = False
scan_timer = 0


def start():
    global timer, scanning, scan_timer
    chunks.clear()
    timer = 0
    scanning = False
    scan_timer = 0
    ship.reset()


def update(keyboard):
    global timer, scanning, scan_timer
    if scanning:
        scan_timer += 1
        if scan_timer > SCAN_FRAMES + FOUND_FRAMES:
            game_states.level_cleared = True
        return

    ship.move(keyboard)
    ship.update_bullets(auto_fire=True)

    timer += 1
    if timer > SPAWN_EVERY:
        chunk = Actor("ice")
        chunk.pos = (random.randint(60, 740), -50)
        chunk.hits = 0  # how many times it has been shot
        chunks.append(chunk)
        timer = 0

    for chunk in chunks[:]:
        chunk.y += CHUNK_SPEED
        if chunk.colliderect(ship.ship):
            ship.play_crash_sound()
            game_states.health -= 1
            chunks.remove(chunk)
        elif chunk.y > 650:
            game_states.health -= 1
            chunks.remove(chunk)
        else:
            for bullet in ship.bullets[:]:
                if chunk.colliderect(bullet):
                    ship.bullets.remove(bullet)
                    chunk.hits += 1
                    if chunk.hits == 1:
                        chunk.image = "ice_cracked"
                    else:
                        game_states.score += 1
                        game_states.level_points += 1
                        chunks.remove(chunk)
                    break

    # Enough ice broken: the path is clear, so stop the ice and start the Scan.
    if game_states.level_points >= LEVELS[game_states.level_number]["target"]:
        scanning = True
        chunks.clear()
        ship.bullets.clear()


def draw(screen):
    background.draw()
    for chunk in chunks:
        chunk.draw()
    if scanning:
        # The scan beam shines from the Ship down onto the ice.
        screen.draw.filled_rect(Rect(ship.ship.x - 15, ship.ship.y + 30, 30, 600), (120, 220, 255))
    ship.draw()
    hud.draw(screen)
    if scanning:
        if scan_timer < SCAN_FRAMES:
            screen.draw.text("Scanning the ice...", center=(400, 220), fontsize=50, color="cyan", owidth=1.5, ocolor="black")
            screen.draw.rect(Rect(250, 260, 300, 26), "white")
            screen.draw.filled_rect(Rect(252, 262, 296 * scan_timer // SCAN_FRAMES, 22), (120, 220, 255))
        else:
            screen.draw.text("Ocean found!", center=(400, 250), fontsize=80, color="yellow", owidth=1.5, ocolor="black")


def on_key_down(key, keys):
    if key == keys.SPACE and not scanning:
        ship.fire()
