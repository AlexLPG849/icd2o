import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaga-like Game")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Player properties
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 100
player_speed = 5
player_health = 3

# Bullet properties
bullet_speed = 10
bullet_width = 5
bullet_height = 10
bullets = []

# Circle properties
circle_radius = 20
circle_speed = 3
circles = []

# Function to draw the player
def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, player_size, player_size))

# Function to draw the bullet
def draw_bullet(x, y):
    pygame.draw.polygon(screen, GREEN, [(x, y), (x + bullet_width, y), (x + bullet_width / 2, y - bullet_height)])

# Function to draw the circle
def draw_circle(x, y):
    pygame.draw.circle(screen, RED, (x, y), circle_radius)

# Function to handle player collision with circles
def player_circle_collision(player_x, player_y, circle_x, circle_y):
    distance = ((player_x - circle_x) ** 2 + (player_y - circle_y) ** 2) ** 0.5
    return distance < (circle_radius + player_size) / 2

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Shooting bullets
    if keys[pygame.K_SPACE]:
        bullets.append([player_x + player_size // 2 - bullet_width // 2, player_y])

    # Move the bullets
    for bullet in bullets:
        bullet[1] -= bullet_speed

    # Generate circles randomly
    if random.randint(0, 100) < 2:
        circle_x = random.randint(0, WIDTH - 2 * circle_radius)
        circles.append([circle_x, -circle_radius])

    # Move the circles
    for circle in circles:
        circle[1] += circle_speed

    # Collision detection for bullets and circles
    for bullet in bullets[:]:
        for circle in circles[:]:
            if (bullet[0] + bullet_width >= circle[0] and bullet[0] <= circle[0] + 2 * circle_radius) and (
                    bullet[1] <= circle[1] + 2 * circle_radius):
                bullets.remove(bullet)
                circles.remove(circle)

    # Collision detection for player and circles
    for circle in circles:
        if player_circle_collision(player_x + player_size // 2, player_y + player_size // 2, circle[0], circle[1]):
            player_health -= 1
            circles.remove(circle)
            if player_health <= 0:
                running = False
                # Game over
                print("Game Over")
                pygame.quit()
                sys.exit()

    # Draw everything
    draw_player(player_x, player_y)
    for bullet in bullets:
        draw_bullet(bullet[0], bullet[1])
    for circle in circles:
        draw_circle(circle[0], circle[1])

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()