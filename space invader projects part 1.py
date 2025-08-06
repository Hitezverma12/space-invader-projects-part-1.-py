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
    distance = 

    