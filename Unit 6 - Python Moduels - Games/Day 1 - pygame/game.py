import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define player properties
player_size = 50
player_x = screen_width // 2 - player_size // 2
player_y = screen_height - player_size - 10
player_speed = 5

# Define item properties
item_size = 30
item_speed = 3
items = []
item_spawn_delay = 50
item_spawn_counter = 0

# Define obstacle properties
obstacle_size = 50
obstacle_speed = 5
obstacles = []
obstacle_spawn_delay = 100
obstacle_spawn_counter = 0

# Define fonts
font = pygame.font.SysFont(None, 36)

# Function to draw the player
def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, [x, y, player_size, player_size])

# Function to draw items
def draw_items(items):
    for item in items:
        pygame.draw.rect(screen, RED, [item[0], item[1], item_size, item_size])

# Function to draw obstacles
def draw_obstacles(obstacles):
    for obstacle in obstacles:
        pygame.draw.rect(screen, BLACK, [obstacle[0], obstacle[1], obstacle_size, obstacle_size])

# Main game loop
running = True
score = 0
while running:
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_size:
        player_x += player_speed

    # Spawn items
    item_spawn_counter += 1
    if item_spawn_counter == item_spawn_delay:
        item_spawn_counter = 0
        item_x = random.randint(0, screen_width - item_size)
        item_y = 0
        items.append([item_x, item_y])

    # Move and draw items
    for item in items:
        item[1] += item_speed
    draw_items(items)

    # Remove items that go off-screen
    items = [item for item in items if item[1] < screen_height]

    # Check for collisions with items
    for item in items:
        if (player_x < item[0] + item_size and
            player_x + player_size > item[0] and
            player_y < item[1] + item_size and
            player_y + player_size > item[1]):
            items.remove(item)
            score += 1

    # Spawn obstacles
    obstacle_spawn_counter += 1
    if obstacle_spawn_counter == obstacle_spawn_delay:
        obstacle_spawn_counter = 0
        obstacle_x = random.randint(0, screen_width - obstacle_size)
        obstacle_y = 0
        obstacles.append([obstacle_x, obstacle_y])

    # Move and draw obstacles
    for obstacle in obstacles:
        obstacle[1] += obstacle_speed
    draw_obstacles(obstacles)

    # Remove obstacles that go off-screen
    obstacles = [obstacle for obstacle in obstacles if obstacle[1] < screen_height]

    # Check for collisions with obstacles
    for obstacle in obstacles:
        if (player_x < obstacle[0] + obstacle_size and
            player_x + player_size > obstacle[0] and
            player_y < obstacle[1] + obstacle_size and
            player_y + player_size > obstacle[1]):
            running = False

    # Draw player
    draw_player(player_x, player_y)

    # Display score
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()