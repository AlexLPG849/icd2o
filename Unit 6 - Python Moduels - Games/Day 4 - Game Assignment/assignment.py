import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (165, 165, 165)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (205, 205, 0)
ORANGE = (255, 165, 0)

# Player properties
player_size = 40
player_speed = 8.5
player_jump_power = 15
player_jump = False
player_jump_count = 10
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size * 2

# Font for game over message
font = pygame.font.Font(None, 64)

# Platform properties
platform_color = GREY
next_level_platform = (65, HEIGHT - 525, 50, 10)
platforms = [
    (0, HEIGHT - 100, WIDTH, 20),      # Ground platform
    (300, HEIGHT - 250, 200, 20),      # Middle platform
    (50, HEIGHT - 500, 300, 20),       # Long platform
    next_level_platform,               # Next level platform
    (500, HEIGHT - 400, 150, 20)       # Upper platform
]

# Spike properties
spikes = [
    (150, HEIGHT - 120, 20, 20),       # Spike set 1
    (130, HEIGHT - 120, 20, 20),
    (170, HEIGHT - 120, 20, 20),
    (150, HEIGHT - 130, 20, 20),
    (600, HEIGHT - 120, 20, 20),       # Spike set 2
    (620, HEIGHT - 120, 20, 20),
    (610, HEIGHT - 140, 20, 20),
    (610, HEIGHT - 420, 20, 20),       # Spike set 3
    (620, HEIGHT - 435, 20, 20),
    (630, HEIGHT - 420, 20, 20),
    (150, HEIGHT - 500, 20, 20),       # Spike set 4
    (130, HEIGHT - 500, 20, 20),
    (170, HEIGHT - 500, 20, 20),
    (150, HEIGHT - 500, 20, 20)
]

# Load sound effects
jump_sound = pygame.mixer.Sound("extraShip.wav")
collision_sound = pygame.mixer.Sound("fire.wav")
level_up_sound = pygame.mixer.Sound("beep.wav")
game_over_sound = pygame.mixer.Sound("thrust.wav")


# Function to reset the game
def reset_game():
    global player_x, player_y, player_jump, game_over, score, current_level
    
    # Reset player position and state
    player_x = WIDTH // 2 - player_size // 2
    player_y = HEIGHT - player_size * 2
    player_jump = False
    
    # Reset game state
    game_over = False
    current_level = 1
    
    # Reset score and clear spikes
    score = 0
    clear_random_spikes()
    respawn_prebuilt_spikes()

# Function to add 1-3 random spikes to random platforms (excluding ground and next level platform)
def add_random_spikes():
    num_spikes = random.randint(1, 3)
    
    # Filter out ground and next level platform from available platforms
    available_platforms = [platform for platform in platforms 
                           if platform != next_level_platform and platform[1] != HEIGHT - 100]
    
    for _ in range(num_spikes):
        if available_platforms:
            random_platform = random.choice(available_platforms)
            spike_x = random.randint(random_platform[0], random_platform[0] + random_platform[2] - 20)
            spike_y = random_platform[1] - 20
            spikes.append((spike_x, spike_y, 20, 20))
            available_platforms.remove(random_platform)

# Function to clear only the randomly generated spikes
def clear_random_spikes():
    global spikes
    spikes = [spike for spike in spikes if not is_prebuilt_spike(spike)]

# Function to check if a spike is a prebuilt spike
def is_prebuilt_spike(spike):
    # Check against the coordinates of prebuilt spikes
    prebuilt_spike_coords = [
        (150, HEIGHT - 120), (130, HEIGHT - 120), (170, HEIGHT - 120), (150, HEIGHT - 130),
        (600, HEIGHT - 120), (620, HEIGHT - 120), (610, HEIGHT - 140),
        (610, HEIGHT - 420), (620, HEIGHT - 435), (630, HEIGHT - 420),
        (150, HEIGHT - 500), (130, HEIGHT - 500), (170, HEIGHT - 500)
    ]
    spike_x, spike_y, _, _ = spike
    return (spike_x, spike_y) in prebuilt_spike_coords

# Function to respawn the prebuilt spikes
def respawn_prebuilt_spikes():
    global spikes
    spikes = [
        (150, HEIGHT - 120, 20, 20),  # Spike set 1
        (130, HEIGHT - 120, 20, 20),
        (170, HEIGHT - 120, 20, 20),
        (150, HEIGHT - 130, 20, 20),
        (600, HEIGHT - 120, 20, 20),  # Spike set 2
        (620, HEIGHT - 120, 20, 20),
        (610, HEIGHT - 140, 20, 20),
        (610, HEIGHT - 420, 20, 20),  # Spike set 3
        (620, HEIGHT - 435, 20, 20),
        (630, HEIGHT - 420, 20, 20),
        (150, HEIGHT - 500, 20, 20),  # Spike set 4
        (130, HEIGHT - 500, 20, 20),
        (170, HEIGHT - 500, 20, 20),
        (150, HEIGHT - 500, 20, 20)
    ]

# Game loop
running = True
game_over = False
game_over_time = 0

current_level = 1
level_colors = {
    1: BLACK,
    2: BLUE,
    3: GREEN,
    4: YELLOW,
    5: ORANGE
}
background_color = level_colors[current_level]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if game_over:
                    reset_game()

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player_x -= player_speed
        if keys[pygame.K_d]:
            player_x += player_speed
        if keys[pygame.K_SPACE] and not player_jump:
            player_jump = True
            jump_sound.play()

        if player_jump:
            if player_jump_count >= -10:
                neg = 1
                if player_jump_count < 0:
                    neg = -1
                player_y -= (player_jump_count ** 2) * 0.5 * neg
                player_jump_count -= 1
            else:
                player_jump = False
                player_jump_count = 10

        player_on_platform = False
        for platform in platforms:
            platform_x, platform_y, platform_width, platform_height = platform
            if (player_y + player_size >= platform_y and player_y <= platform_y + platform_height
                    and player_x + player_size >= platform_x and player_x <= platform_x + platform_width):
                player_y = platform_y - player_size
                player_on_platform = True
                if platform == next_level_platform:
                    current_level += 1  # Increase level by 1 when reaching next level platform
                    if current_level in level_colors:
                        background_color = level_colors[current_level]
                    else:
                        background_color = BLACK
                    reset_game()  # Reset the game state for the next level
                    if current_level > 5:
                        game_over = True  # Game ends after reaching level 5 (orange)
                        game_over_time = pygame.time.get_ticks()
                    else:
                        add_random_spikes()  # Add 1-3 random spikes to random platforms
                        level_up_sound.play()  # Play level up sound effect
                break

        for spike in spikes:
            spike_x, spike_y, spike_width, spike_height = spike
            if (player_x + player_size >= spike_x and player_x <= spike_x + spike_width
                    and player_y + player_size >= spike_y and player_y <= spike_y + spike_height):
                game_over = True
                game_over_time = pygame.time.get_ticks()
                collision_sound.play()
                break

        if not player_on_platform:
            player_y += player_speed

        if player_x < 0:
            player_x = 0
        elif player_x > WIDTH - player_size:
            player_x = WIDTH - player_size

    screen.fill(background_color)
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_size, player_size))
    for platform in platforms:
        pygame.draw.rect(screen, platform_color, platform)
    for spike in spikes:
        pygame.draw.rect(screen, RED, spike)

    # Display current level
    level_text = font.render("Level: " + str(current_level), True, WHITE)
    screen.blit(level_text, (10, 10))

    if game_over:
        game_over_text = font.render("Game Over", True, WHITE)
        text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(game_over_text, text_rect)

        if pygame.time.get_ticks() - game_over_time >= 2000:
            play_again_text = font.render("Play again? (Enter to continue)", True, WHITE)
            text_rect = play_again_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
            screen.blit(play_again_text, text_rect)

    pygame.display.update()
    pygame.time.delay(15)

# Clean up and exit
pygame.mixer.quit()
pygame.quit()
sys.exit()