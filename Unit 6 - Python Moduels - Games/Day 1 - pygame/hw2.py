import sys
import pygame
# Initialize Pygame
pygame.init()
# Set up the display
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SHip")
# Define RGB colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
# Main loop
while True:
    screen.fill((255, 255, 255))  # Fill the screen with white color
    # Draw colored rectangles
    pygame.draw.rect(screen, blue, (50, 50, 100, 300))  # Main body
    pygame.draw.polygon(screen, cyan, [(50, 50), (150, 50), (100, 0)])  # Tip of the rocket
    pygame.draw.rect(screen, red, (25, 200, 50, 20))  # Left wing
    pygame.draw.rect(screen, red, (125, 200, 50, 20))  # Right wing
    # Update the display
    pygame.display.flip()
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()