import sys
import pygame
# Initialize Pygame
pygame.init()
# Set up the display
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flag")
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
    pygame.draw.rect(screen, red, (50, 50, 20, 150))  # Flagpole
    pygame.draw.rect(screen, blue, (70, 50, 100, 60))  # Flag
    pygame.draw.lines(screen, magenta, False, [(70, 50), (170, 50)], 4)  # Stripes
    # Update the display
    pygame.display.flip()
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.draw.rect(screen, blue, (100, 300, 200, 200))  # Main body
    pygame.draw.polygon(screen, red, [(100, 300), (300, 300), (200, 200)])  # Roof
    pygame.draw.rect(screen, green, (160, 400, 80, 100))  # Door
    pygame.draw.circle(screen, yellow, (250, 370), 20)  # Window
    pygame.draw.circle(screen, yellow, (150, 370), 20)  # Window