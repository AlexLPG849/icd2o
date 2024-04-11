import sys
import pygame
# Initialize Pygame
pygame.init()
# Set up the display
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("House")
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
    pygame.draw.rect(screen, grey, (100, 300, 200, 200))  # Main body
    pygame.draw.polygon(screen, black, [(100, 300), (300, 300), (200, 200)])  # Roof
    pygame.draw.rect(screen, brown, (160, 400, 80, 100))  # Door
    pygame.draw.circle(screen, cyan, (250, 370), 20)  # Window
    pygame.draw.circle(screen, cyan, (150, 370), 20)  # Window
    # Update the display
    pygame.display.flip()
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()