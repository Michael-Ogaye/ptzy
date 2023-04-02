import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

# Set the window title
pygame.display.set_caption("Whac-A-Mole")

# Create the window
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set the background color
BACKGROUND_COLOR = (255, 255, 255)
screen.fill(BACKGROUND_COLOR)

# Load the mole image
MOLE_IMAGE = pygame.image.load("mole.png")

# Load the hammer image
HAMMER_IMAGE = pygame.image.load("hammer.png")

# Set the number of moles to appear
NUM_MOLES = 10

# Set the duration of the game in seconds
GAME_DURATION = 30

# Define the Mole class
class Mole(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = MOLE_IMAGE
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WINDOW_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, WINDOW_HEIGHT - self.rect.height)

    def update(self):
        self.rect.x = random.randint(0, WINDOW_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, WINDOW_HEIGHT - self.rect.height)

# Define the Hammer class
class Hammer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = HAMMER_IMAGE
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

# Create a group of moles
mole_group = pygame.sprite.Group()
for i in range(NUM_MOLES):
    mole = Mole()
    mole_group.add(mole)

# Create the hammer
hammer = Hammer()

# Set the game clock
clock = pygame.time.Clock()

# Set the start time of the game
start_time = pygame.time.get_ticks()

# Set the score
score = 0

# Set the font
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the hammer hit a mole
            hits = pygame.sprite.spritecollide(hammer, mole_group, True)
            if hits:
                score += len(hits)

    # Update the game objects
    mole_group.update()
    hammer.update()

    # Draw the game objects
    screen.fill(BACKGROUND_COLOR)
    mole_group.draw(screen)
    screen.blit(hammer.image, hammer.rect)

    # Draw the score
    score_text = font.render("Score: {}".format(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Check if the game is over
    elapsed_time = pygame.time.get_ticks() - start_time
    if elapsed_time > GAME_DURATION * 1000:
        running = False

    # Update the screen
    pygame.display.update()

    # Limit the frame rate
    clock.tick(30)

# Game over
game_over_text = font.render("Game Over", True, (0, 0, 0))
screen.blit(game_over_text, )
