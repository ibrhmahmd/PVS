import pgzrun
from pgzero.actor import Actor
import random
import pygame
from game_data import space_info_list

high_score = 0
level = 1  
WIDTH = 800
HEIGHT = 600
FULLSCREEN = True

background = Actor("backgrounds/space_background", (400, 300))
ship = Actor("characters/ship", (400, 550))


ship.scale = 0.5
bullets = []
asteroids = []
heart = Actor("health")
heart.scale = 0.1

logo = Actor("logogame")
logo.scale = 0.5
logo.pos = (400,250)


score = 0
health = 3
timer = 0
game_started = False
current_planet_info = None
current_planet_image = None
show_info_screen = False
paused = False

def draw():
    background.draw()

    if not game_started:
        logo.draw()
        screen.draw.text("SpaceX is an educational game to learn about our solar system", center=(400, 500), fontsize=35, color="yellow")
        screen.draw.text("Press Space to Start", center=(400, 550), fontsize=60, color="white")
        return

    ship.draw()
    for bullet in bullets:
        bullet.draw()
    if health > 0:
        for asteroid in asteroids:
            asteroid.draw()
    for i in range(max(0, health)):
        heart.pos = (WIDTH - 40 - (i * 50), 40)
        heart.draw()
    screen.draw.text(f"Score: {score}", topleft=(20, 20), fontsize=50, color="yellow")
    screen.draw.text(f"Level: {level}", bottomright=(WIDTH - 20, HEIGHT - 20), fontsize=40, color="cyan")
    screen.draw.text(f"High Score: {high_score}", bottomleft=(20, HEIGHT - 20), fontsize=40, color="cyan")
    
    if paused:
        screen.draw.text("PAUSED", center=(400, 300), fontsize=80, color="orange")
        screen.draw.text("press P to continue", center=(400, 400), fontsize=40, color="white")
        music.stop()

    if health <= 0:
                
        if show_info_screen and current_planet_info:
            center_x = WIDTH // 2
            center_y = HEIGHT // 2
            
            if current_planet_image:
                img_rect = current_planet_image.get_rect()
                img_rect.center = (center_x, center_y - 150)
                screen.surface.blit(current_planet_image, img_rect)
            
            text_content = " ".join(current_planet_info["text"])
            screen.draw.text(text_content, 
                           midtop=(center_x, center_y - 20),
                           width=700,
                           fontsize=40,
                           color="white",
                           align="center",
                           shadow=(1,1),
                           scolor="black")
        
        screen.draw.text("GAME OVER", center=(400, 480), fontsize=120, color="red")        
        screen.draw.text("Press R to Restart", center=(400, 550), fontsize=50, color="white")

def update():
    global score, health, timer, current_planet_info, show_info_screen, current_planet_image, high_score, level, game_started, paused
    
    if not game_started or paused:
        return
    
    if health > 0 and not music.is_playing('music.mp3'):
        music.play('music.mp3')
        music.set_volume(0.9)

    if health <= 0 and music.is_playing('music.mp3'):
        music.stop()

    if health <= 0:
        if not show_info_screen:
            if score > high_score:
                high_score = score
            current_planet_info = random.choice(space_info_list)
            current_planet_image = pygame.image.load(current_planet_info["image"])
            show_info_screen = True
        return
    level = 1 + score // 30
    if keyboard.left and ship.x > 50:  
        ship.x -= 9
    if keyboard.right and ship.x < 750: 
        ship.x += 9

    # adding forward and backward movement Feature  

    # if keyboard.up and ship.y > 50: 
    #     ship.y -= 8
    # if keyboard.down and ship.y < 550: 
    #     ship.y += 8

    for bullet in bullets[:]:
        bullet.y -= 10
        if bullet.y < -50:
            bullets.remove(bullet)
    timer += 1
    spawn_time = max(20, 60 - int(score / 2))
    if timer > spawn_time:
        asteroid = Actor("asteroid")
        asteroid.pos = (random.randint(50, 750), -50)
        asteroid.scale = 0.4
        asteroids.append(asteroid)
        timer = 0
    for asteroid in asteroids[:]:
        speed = 3 + min(score / 10, 5)
        asteroid.y += speed

        if asteroid.colliderect(ship):
            crash_sound = pygame.mixer.Sound('music/crash.mp3')
            crash_sound.set_volume(0.4)
            crash_sound.play()
            health -= 1
            asteroids.remove(asteroid)        
        elif asteroid.y > 650:
            health -= 1
            asteroids.remove(asteroid)
        else:
            for bullet in bullets[:]:
                if asteroid.colliderect(bullet):
                    score += 1
                    if asteroid in asteroids:
                        asteroids.remove(asteroid)
                    if bullet in bullets:
                        bullets.remove(bullet)
                    break

def on_key_down(key):
    global score, health, asteroids, bullets, timer, show_info_screen, current_planet_info, level, game_started, paused

    if key == keys.P and game_started and health > 0:
        paused = not paused

    if paused:
        return

    if key == keys.SPACE:
        if not game_started:
            game_started = True
        else:
            new_bullet = Actor("bullet")
            new_bullet.scale = 0.3
            new_bullet.pos = ship.x, ship.y
            bullets.append(new_bullet)
    if key == keys.R and health <= 0:
        score = 0
        health = 3
        level = 1
        asteroids = []
        bullets = []
        timer = 0
        show_info_screen = False
        current_planet_info = None
    if key == keys.F:
        pygame.display.toggle_fullscreen()

pgzrun.go()
