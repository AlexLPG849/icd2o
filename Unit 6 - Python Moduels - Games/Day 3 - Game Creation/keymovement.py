import sys
#sys.path.append('C:\\Python312\\Lib\\site-packages')
import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Key Mover")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Define game variables
clock = pygame.time.Clock()

player_radius = 10
player_color = BLUE
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_speed = 5
game_over = False

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


     # Control the frame rate
    clock.tick(60)  # Set the frame rate to 60 frames per second
    
    # Move player circle with keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
        player_x = max(player_x, player_radius)  # Ensure player does not move off the left edge
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
        player_x = min(player_x, SCREEN_WIDTH - player_radius)  # Ensure player does not move off the right edge
    if keys[pygame.K_UP]:
        player_y -= player_speed
        player_y = max(player_y, player_radius)  # Ensure player does not move off the top edge
    if keys[pygame.K_DOWN]:
        player_y += player_speed
        player_y = min(player_y, SCREEN_HEIGHT - player_radius)  # Ensure player does not move off the bottom edge

    # Draw player circle
    pygame.draw.circle(screen, player_color, (player_x, player_y), player_radius)

   

    # Refresh screen
    pygame.display.flip()


pygame.quit()
sys.exit()