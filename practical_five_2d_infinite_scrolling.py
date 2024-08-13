import pygame
import sys
# Initialize Pygame
pygame.init()
# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
# Load background image
background = pygame.image.load('game.jpeg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Scale to fit the window
# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Infinite Scrolling Background")
# Variables for background scrolling
y1 = 0
y2 = -HEIGHT  # Second background image positioned above the first one
# Main game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Scroll the background
    y1 += 1
    y2 += 1
    # Reset background positions when they move off screen
    if y1 >= HEIGHT:
        y1 = -HEIGHT
    if y2 >= HEIGHT:
        y2 = -HEIGHT
    # Draw the background images
    screen.blit(background, (0, y1))
    screen.blit(background, (0, y2))
    # Update the display
    pygame.display.flip()
    # Cap the frame rate
    clock.tick(FPS)
