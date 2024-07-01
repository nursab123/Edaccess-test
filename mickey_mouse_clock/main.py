import pygame
import sys
import math
from datetime import datetime

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
WHITE = (255, 255, 255)
CENTER = (WIDTH // 2, HEIGHT // 2)
CLOCK_RADIUS = 350

# Load images
mickey_img = pygame.image.load('main_clock.png')  # Path to Mickey Mouse image without hands
left_hand_img = pygame.image.load('left_hand.png')  # Path to Mickey's left hand image
right_hand_img = pygame.image.load('right_hand.png')  # Path to Mickey's right hand image

# Resize images if necessary
mickey_img = pygame.transform.scale(mickey_img, (600, 600))

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mickey Mouse Clock')

def blit_rotate_center(surf, image, topleft, angle):
    """Rotate an image and blit it to the screen."""
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)
    surf.blit(rotated_image, new_rect.topleft)

def get_angle(unit, max_unit):
    """Calculate the angle for the hand rotation."""
    return (unit / max_unit) * 360

def main():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get current time
        now = datetime.now()
        seconds = now.second
        minutes = now.minute

        # Calculate angles
        second_angle = get_angle(seconds, 60)
        minute_angle = get_angle(minutes, 60)

        # Draw background
        screen.fill(WHITE)
        
        # Draw Mickey's body
        screen.blit(mickey_img, (CENTER[0] - mickey_img.get_width() // 2, CENTER[1] - mickey_img.get_height() // 2))

        # Draw hands
        blit_rotate_center(screen, left_hand_img, (CENTER[0], CENTER[1]), -second_angle)
        blit_rotate_center(screen, right_hand_img, (CENTER[0], CENTER[1]), -minute_angle)

        pygame.display.flip()
        clock.tick(60)