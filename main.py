import pygame
import random
import sys

pygame.init()

GRID_SIZE = 20
GRID_COUNT = 20
WINDOW_SIZE = GRID_SIZE * GRID_COUNT  # 400x400 pixels

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Lab 3: Snake Game")
clock = pygame.time.Clock()

BACKGROUND_COLOR = (30, 30, 40)
SNAKE_COLOR = (46, 204, 113)
FOOD_COLOR = (231, 76, 60)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    pygame.display.flip()
    
    clock.tick(10)

pygame.quit()
sys.exit()
