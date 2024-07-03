import pygame
from datetime import datetime
import math

RES = WIDTH, HEIGHT = 1200, 800
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2
RADIUS = H_HEIGHT - 50
radius_list = {'sec': RADIUS - 10, 'min': RADIUS - 55, 'digit': RADIUS - 30}

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

clock60 = dict(zip(range(60), range(0, 360, 6)))  # for minutes and seconds

font = pygame.font.SysFont('Verdana', 60)

#Load images
body_img = pygame.image.load('main-clock.png').convert_alpha()
right_hand_img = pygame.image.load('right-hand.png').convert_alpha()
left_hand_img = pygame.image.load('left-hand.png').convert_alpha()

def get_clock_pos(clock_dict, clock_hand, key):
    x = H_WIDTH + radius_list[key] * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = H_HEIGHT + radius_list[key] * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y

def blit_rotate_center(surf, image, center, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    surf.blit(rotated_image, new_rect.topleft)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    # set background
    surface.fill(pygame.Color('white'))
    #get time now
    t = datetime.now()
    minute = t.minute
    second = t.second
    #draw clock face
    pygame.draw.circle(surface, pygame.Color('yellow'), (H_WIDTH, H_HEIGHT), RADIUS)
    surface.blit(body_img, body_img.get_rect(center=(H_WIDTH, H_HEIGHT)))

    for digit, pos in clock60.items():
        radius = 20 if not digit % 3 and not digit % 5 else 8 if not digit % 5 else 2
        pygame.draw.circle(surface, pygame.Color('gainsboro'), get_clock_pos(clock60, digit, 'digit'), radius, 7)

    #draw Mickey's hands
    minute_angle = -clock60[minute] # Rotate counterclockwise
    second_angle = -clock60[second] # Rotate counterclockwise
    blit_rotate_center(surface, right_hand_img, (H_WIDTH, H_HEIGHT), minute_angle)
    blit_rotate_center(surface, left_hand_img, (H_WIDTH, H_HEIGHT), second_angle)

    #digital clock
    time_render = font.render(f'{t:%H:%M:%S}', True, pygame.Color('forestgreen'), pygame.Color('orange'))
    surface.blit(time_render, (0, 0))

    pygame.display.flip()
    clock.tick(20)