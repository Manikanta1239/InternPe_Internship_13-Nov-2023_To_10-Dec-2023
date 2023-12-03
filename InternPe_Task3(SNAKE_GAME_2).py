import pygame
import random

pygame.init()

WDT, HGT = 640, 480
GRID_SIZE = 20
SPD = 9

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

window = pygame.display.set_mode((WDT, HGT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

snake = [(WDT / 2, HGT / 2)]
dx, dy = GRID_SIZE, 0

food = (random.randint(0, (WDT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
        random.randint(0, (HGT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)

score = 0
font = pygame.font.Font(None, 36)
game_over = False
running = True
while running:
    window.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -GRID_SIZE
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, GRID_SIZE
            elif event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -GRID_SIZE, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = GRID_SIZE, 0

    if not game_over:
        snake.insert(0, (snake[0][0] + dx, snake[0][1] + dy))
        if (snake[0][0] < 0 or snake[0][0] >= WDT
                or snake[0][1] < 0 or snake[0][1] >= HGT):
            game_over = True
        if len(snake) > 1 and snake[0] in snake[1:]:
            game_over = True
        if snake[0] == food:
            score += 1
            food = (random.randint(0, (WDT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
                    random.randint(0, (HGT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)
        else:
            snake.pop()

        pygame.draw.rect(window, RED, (*food, GRID_SIZE, GRID_SIZE))
        for segment in snake:
            pygame.draw.rect(window, GREEN, (*segment, GRID_SIZE, GRID_SIZE))

        text = font.render(f"Score: {score}", True, WHITE)
        window.blit(text, (10, 10))
    else:
        text = font.render("Game Over! Press Q to quit.", True, WHITE)
        window.blit(text, (WDT // 2 - 150, HGT // 2 - 20))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            snake = [(WDT / 2, HGT / 2)]
            dx, dy = GRID_SIZE, 0
            score = 0
            game_over = False

    pygame.display.update()
    clock.tick(SPD)

pygame.quit()
