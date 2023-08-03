import socket
import pygame
from pygame.locals import *
import time
import pygame
import button

#create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Blimp Base Station")

#load button images
left_arrow_img = pygame.image.load('left_arrow.png').convert_alpha()
up_arrow_img = pygame.image.load('up_arrow.png').convert_alpha()
right_arrow_img = pygame.image.load('right_arrow.png').convert_alpha()
down_arrow_img = pygame.image.load('down_arrow.png').convert_alpha()

#create button instances
left_arrow = button.Button(100, 200, left_arrow_img, 1)
forward_arrow = button.Button(200, 200, up_arrow_img, 1)
right_arrow = button.Button(300, 200, right_arrow_img, 1)
up_arrow = button.Button(500, 200, up_arrow_img, 1)
down_arrow = button.Button(500, 300, down_arrow_img, 1)

#game loop
run = True
while run:

    screen.fill((202, 228, 241))

    if left_arrow.draw(screen):
        print('LEFT')
    if right_arrow.draw(screen):
        print('RIGHT')
    if forward_arrow.draw(screen):
        print('FORWARD')

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()