import sys
import pygame
# Initialize Pygame
pygame.init()
# Set up the display
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SNowman")
# Define RGB colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
white = (255, 255, 255)
black = (0, 0, 0)
# Main loop
while True:
    screen.fill((255, 255, 255))  # Fill the screen with white color
    pygame.draw.circle(screen, yellow, (600, 300), 80)  # Bottom part
    pygame.draw.circle(screen, yellow, (600, 200), 60)  # Middle part
    pygame.draw.circle(screen, yellow, (600, 120), 40)  # Top part
    pygame.draw.circle(screen, black, (585, 110), 5)  # Left eye
    pygame.draw.circle(screen, black, (615, 110), 5)  # Right eye
    pygame.draw.arc(screen, black, (580, 130, 40, 20), 0, 3.14, 3)  # Mouth
    pygame.draw.rect(screen, black, (580, 80, 40, 20))  # Hat
    # Update the display
    pygame.display.flip()
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()