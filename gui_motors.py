import RPi.GPIO as GPIO
import socket
import pygame
from pygame.locals import *
import time
import pygame
import button

# Setting GPIO pins to be referred to their BOARD number (1-40)
GPIO.setmode(GPIO.BOARD)

# Disable warnings
GPIO.setwarnings(False)	

# Setting up the GPIO pins
GPIO.setup(18, GPIO.OUT) # top
GPIO.setup(8, GPIO.OUT)  # left
GPIO.setup(40, GPIO.OUT) # right

# Setting frequency (frequency of PWM / How long one period is)
freq1 = freq2 = freq3 = 1000

# Create PWM Object
top = GPIO.PWM(18, freq1)
left = GPIO.PWM(8, freq2)
right = GPIO.PWM(40, freq3)

# Start PWM generation of a specified duty cycle
top.start(0)
left.start(0)
right.start(0)

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
        left.ChangeDutyCycle(0)
        right.ChangeDutyCycle(0)
        print('LEFT')
        left.ChangeDutyCycle(10)
    if right_arrow.draw(screen):
        left.ChangeDutyCycle(0)
        right.ChangeDutyCycle(0)
        print('RIGHT')
        right.ChangeDutyCycle(10)
    if forward_arrow.draw(screen):
        left.ChangeDutyCycle(0)
        right.ChangeDutyCycle(0)
        print('FORWARD')
        left.ChangeDutyCycle(10)
        right.ChangeDutyCycle(10)

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()