import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sunny Day")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (0, 100, 255)
GREEN = (0, 128, 0)
DARK_GREEN = (0, 100, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (164, 164, 164)
BLEU = (50, 75, 255)
BROWN = (165, 154, 53)
screen.fill(BLEU)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Grass
    pygame.draw.rect(screen, DARK_GREEN, (0, 550, WIDTH, 50))

    # House
    pygame.draw.rect(screen, GRAY, (250, 300, 300, 250))
    pygame.draw.polygon(screen, BLACK, [(250, 300), (550, 300), (400, 150)])
    pygame.draw.rect(screen, BROWN, (370, 420, 60, 130))
    pygame.draw.circle(screen, BLACK, (420, 520), 5)
    pygame.draw.rect(screen, LIGHT_BLUE, (295, 400, 60, 60))
    pygame.draw.rect(screen, LIGHT_BLUE, (450, 400, 60, 60))
    pygame.draw.circle(screen, YELLOW, (WIDTH - 100, 100), 50)
    pygame.draw.circle(screen, WHITE, (WIDTH - 100, 100), 60, 5)
    
    pygame.display.flip()

pygame.quit()
sys.exit()
