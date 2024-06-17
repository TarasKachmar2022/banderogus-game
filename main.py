import random

import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_RIGHT, K_LEFT

pygame.init()

FPS = pygame.time.Clock()

WIDTH = 1200
HEIGHT = 800

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

player_size = (20, 20)
player = pygame.Surface(player_size)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()
# player_speed = [1, 1]

player_move_top = [0, -1]
player_move_right = [1, 0]
player_move_down = [0, 1]
player_move_left = [-1, 0]

enemy_size = (30, 30)
enemy = pygame.Surface(enemy_size)
enemy.fill(COLOR_BLUE)
enemy_rect = pygame.Rect(WIDTH, 100, *enemy_size)
enemy_move = [-1, 0]

playing = True

while playing:
        FPS.tick(660)

        for event in pygame.event.get():
                if event.type == QUIT:
                        playing = False

        main_display.fill(COLOR_BLACK)

        keys = pygame.key.get_pressed()

        if keys[K_UP] and player_rect.top > 0:
                player_rect = player_rect.move(player_move_top)

        if keys[K_RIGHT] and player_rect.right < WIDTH:
                player_rect = player_rect.move(player_move_right)

        if keys[K_DOWN] and player_rect.bottom < HEIGHT:
                player_rect = player_rect.move(player_move_down)
                
        if keys[K_LEFT] and player_rect.left > 0:
                player_rect = player_rect.move(player_move_left)

        enemy_rect = enemy_rect.move(enemy_move)

# Рандомна зміна напрямку
        # if player_rect.top <= 0:
        #         player_speed = random.choice(([-1, 1], [1, 1]))

        # if player_rect.right >= WIDTH:
        #         player_speed = random.choice(([-1, -1], [-1, 1]))

        # if player_rect.bottom >= HEIGHT:
        #         player_speed = random.choice(([1, -1], [-1, -1]))

        # if player_rect.left <= 0:
        #         player_speed = random.choice(([1, 1], [1, -1]))

        main_display.blit(player, player_rect)

        main_display.blit(enemy, enemy_rect)

        # player_rect = player_rect.move(player_speed)

        pygame.display.flip()