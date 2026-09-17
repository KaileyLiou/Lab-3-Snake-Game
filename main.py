import pygame
import random
import sys

pygame.init()

GRID_SIZE = 30
GRID_COUNT = 30
WINDOW_SIZE = GRID_SIZE * GRID_COUNT  # 400x400 pixels

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Lab 3: Snake Game")
clock = pygame.time.Clock()

BACKGROUND_COLOR = (50, 168, 82)
SNAKE_COLOR = (39, 135, 245)
FOOD_COLOR = (231, 76, 60)

running = True

# starts at (5, 10) with a 3-block body length
snake_body = [[5, 10], [4, 10], [3, 10]]
snake_direction = "RIGHT"

# places food at a random grid block
food_position = [random.randint(0, GRID_COUNT - 1), random.randint(0, GRID_COUNT - 1)]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and snake_direction != "DOWN":
                snake_direction = "UP"
            elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and snake_direction != "UP":
                snake_direction = "DOWN"
            elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and snake_direction != "LEFT":
                snake_direction = "RIGHT"

    head_x, head_y = snake_body[0][0], snake_body[0][1]
    if snake_direction == "UP":
        head_y -= 1
    elif snake_direction == "DOWN":
        head_y += 1
    elif snake_direction == "LEFT":
        head_x -= 1
    elif snake_direction == "RIGHT":
        head_x += 1
    new_head = [head_x, head_y]

    if head_x < 0 or head_x >= GRID_COUNT or head_y < 0 or head_y >= GRID_COUNT:
        print("Game Over: You hit the wall!")
        running = False
        continue

    if new_head in snake_body:
        print("Game Over: You bit yourself!")
        running = False
        continue

    snake_body.insert(0, new_head)

    if new_head == food_position:
        food_position = [random.randint(0, GRID_COUNT - 1), random.randint(0, GRID_COUNT - 1)]
    else:
        snake_body.pop()

    screen.fill(BACKGROUND_COLOR)

    food_rect = pygame.Rect(food_position[0] * GRID_SIZE, food_position[1] * GRID_SIZE, GRID_SIZE - 2, GRID_SIZE - 2)
    pygame.draw.rect(screen, FOOD_COLOR, food_rect)

    for segment in snake_body:
        segment_rect = pygame.Rect(segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE - 2, GRID_SIZE - 2)
        pygame.draw.rect(screen, SNAKE_COLOR, segment_rect)

    pygame.display.flip()
    
    clock.tick(10)

pygame.quit()
sys.exit()
