import sys
import pygame
# Initialize Pygame
pygame.init()
# Set up the display
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("suhn")
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
    pygame.draw.circle(screen, yellow, (700, 500), 80)  # Sun
    pygame.draw.lines(screen, yellow, False, [(630, 500), (660, 500)], 4)  # Rays
    pygame.draw.lines(screen, yellow, False, [(740, 500), (770, 500)], 4)  # Rays
    pygame.draw.lines(screen, yellow, False, [(700, 430), (700, 460)], 4)  # Rays
    pygame.draw.lines(screen, yellow, False, [(700, 570), (700, 540)], 4)  # Rays
    # Update the display
    pygame.display.flip()
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()