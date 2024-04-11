import sys
import pygame
# Initialize Pygame
pygame.init()
# Set up the display
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tree")
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
      # Draw the trunk (rectangle)
    pygame.draw.rect(screen, brown, (180, 250, 40, 100))  # (x, y, width, height)
    
    # Draw the leaves (triangle)
    pygame.draw.polygon(screen, green, [(100, 250), (200, 100), (300, 250)])
    pygame.draw.polygon(screen, green, [(120, 200), (200, 50), (280, 200)])
    pygame.draw.polygon(screen, green, [(140, 150), (200, 20), (260, 150)])
    # Update the display
    pygame.display.flip()
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()