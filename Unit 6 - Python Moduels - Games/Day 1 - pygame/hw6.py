import sys
import pygame
# Initialize Pygame
pygame.init()
# Set up the display
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car")
# Define RGB colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
grey = (165, 165, 165)
brown = (165, 42, 42)
black = (1, 1, 0)
# Main loop
while True:
    screen.fill((255, 255, 255))  # Fill the screen with white color
    # Draw colored rectangles
    pygame.draw.rect(screen, red, (400, 450, 300, 100))  # Main body
    pygame.draw.rect(screen, blue, (450, 470, 40, 30))  # Window
    pygame.draw.rect(screen, blue, (570, 470, 40, 30))  # Window
    pygame.draw.circle(screen, black, (450, 550), 30)  # Front wheel
    pygame.draw.circle(screen, black, (650, 550), 30)  # Back wheel
    # Update the display
    pygame.display.flip()
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()