import math
import random
import pygame

screen_width = 800
screen_height = 500
player_start_x = 370
player_start_y = 380

enemy_start_y_min = 50
enemy_start_y_max = 150

enemy_speed_x = 4 
enemy_speed_y = 40
bullet_speed_y = 10
collisision_radius = 27

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
backround = pygame.image.load('background.png')

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('icon.png ') 

playerImg = pygame.image.load('player.png')
playerx = player_start_x
playery = player_start_y

playerx_change = 0
enemyImg = []
enemyx = []
enemyy = []

enemyx_change = []
enemyy_change = []
num_of_enemies = 6  

for _i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyx.append(random.randint(enemy_start_y_min, screen_width - 64))

    enemyy.append(random.randint(enemy_start_y_min,enemy_start_y_max))
    enemyx_change.append(enemy_speed_x)
    enemyy_change.append(enemy_speed_y)
bullentImg = pygame.image.load('bullet.png')
bulletx = 0

bullety = player_start_y
bulletx_change = 0
bullety_change = bullet_speed_y
bullet_state = "ready"

score_value = 0

font = pygame.font.Font('freesanbold.ttf', 32)
textX = 10
textY = 10
over_font = pygame.font.Font('freesanbold.ttf', 64)
def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text,(200,250))
def player(x, y):
    screen.blit(playerImg, (x, y))
def enemy(x, y, i):
    screen.billt(enemyImg[i], (x, y))
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullentImg, (x + 16, y + 10))
def is_collision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt((enemyx - bulletx)) ** 2 + ((enemyy- bullety) ** 2)
    return distance < collisision_radius

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(backround, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -5
            if event.key == pygame.K_RIGHT:
                playerx_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletx = playerx
                    fire_bullet(bulletx, bullety)
        if event.type == pygame.KEYUP and event.key in (pygame.K_LEFT, pygame.K_RIGHT):
            playerx_change = 0
    playerx += playerx_change
    playerx = max(0, min(playerx, screen_width - 64))

    for i in range(num_of_enemies):
        if enemyy[i] > 440:
            for j in range(num_of_enemies):
                enemyy[j] = 2000
            game_over_text()
            break


        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0 or enemyx[i] >= screen_width - 64:

            enemyx[i] *= -1
            enemyx_change[i] += enemyy_change[i]
            enemyy[i] += enemyy_change[i]

        if iscollision(enemyx[i], enemyy[i], bulletx, bullety)
    
            bullety = player_start_y
            bullet_state = "ready"
            score_value += 1
            enemyx[i] = random.randint(0, screen_width - 64)
            enemyy[i] = random.randint(enemy_start_y_min, enemy_start_y_min)


        enemy(enemyx[i], enemyy[i], i)

        if bullety <= 0:
            bullety = player_start_y
            bullet_state = "ready"
        if bullet_state == "fire":
            fire_bullet(bulletx, bullety)
            bullety -= bullety_change
player(playerx, playery)
show_score(textX, textY)
pygame.display.update()

    