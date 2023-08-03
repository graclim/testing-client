# -------------------- IMPORTS --------------------
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

# -------------------- MOTORS --------------------

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

# -------------------- LED --------------------

# Setting up the GPIO pins
GPIO.setup(26, GPIO.OUT) # LED Blue
GPIO.setup(36, GPIO.OUT) # LED Green
GPIO.setup(32, GPIO.OUT) # LED Red

LEDPinBlue = 26
LEDPinGreen = 36
LEDPinRed = 32

# Create PWM Object
blue = GPIO.PWM(LEDPinBlue, 1000)
green = GPIO.PWM(LEDPinGreen, 1000)
red = GPIO.PWM(LEDPinRed, 1000)

# Start PWM generation of a specified duty cycle
blue.start(0)
green.start(0)
red.start(0)

# -------------------- SETTING UP GUI --------------------

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 870

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Blimp Base Station")

# -------------------- IMAGES --------------------

# Arrow Images
left_arrow_img = pygame.image.load('arrows/left_arrow.png').convert_alpha()
up_arrow_img = pygame.image.load('arrows/up_arrow.png').convert_alpha()
right_arrow_img = pygame.image.load('arrows/right_arrow.png').convert_alpha()
down_arrow_img = pygame.image.load('arrows/down_arrow.png').convert_alpha()

# Exit Image
exit_img = pygame.image.load('buttons/exit_btn.png').convert_alpha()

# Modes Images - ON
manual_img_on = pygame.image.load('buttons/button_manual_on.png').convert_alpha()
waypoint_img_on = pygame.image.load('buttons/button_waypoint_on.png').convert_alpha()
auto_img_on = pygame.image.load('buttons/button_auto_on.png').convert_alpha()

# Modes Images - OFF
manual_img_off = pygame.image.load('buttons/button_manual_off.png').convert_alpha()
waypoint_img_off = pygame.image.load('buttons/button_waypoint_off.png').convert_alpha()
auto_img_off = pygame.image.load('buttons/button_auto_off.png').convert_alpha()

# Extra Images - ON
apriltags_img_on = pygame.image.load('buttons/button_apriltags_on.png').convert_alpha()
tof_img_on = pygame.image.load('buttons/button_tof_on.png').convert_alpha()
projector_img_on = pygame.image.load('buttons/button_projector_on.png').convert_alpha()

# Extra Images - OFF
apriltags_img_off = pygame.image.load('buttons/button_apriltags_off.png').convert_alpha()
tof_img_off = pygame.image.load('buttons/button_tof_off.png').convert_alpha()
projector_img_off = pygame.image.load('buttons/button_projector_off.png').convert_alpha()

# On and Off Images
button_on = pygame.image.load('buttons/button_on.png').convert_alpha()
button_off = pygame.image.load('buttons/button_off.png').convert_alpha()

# -------------------- BUTTONS --------------------

# Arrow Buttons
left_arrow = button.Button(100, 280, left_arrow_img, 1)
forward_arrow = button.Button(200, 280, up_arrow_img, 1)
right_arrow = button.Button(300, 280, right_arrow_img, 1)
up_arrow = button.Button(450, 280, up_arrow_img, 1)
down_arrow = button.Button(450, 380, down_arrow_img, 1)

# Exit Button
exit_button = button.Button(790, 10, exit_img, 0.3)

# Modes Buttons
manual_button = button.Button(100, 400, manual_img_on, 0.5)
waypoint_button = button.Button(200, 400, waypoint_img_off, 0.5)
auto_button = button.Button(300, 400, auto_img_off, 0.5)

# Extra Buttons
apriltags_button = button.Button(600, 100, apriltags_img_off, 0.5)
tof_button = button.Button(600, 175, tof_img_off, 0.5)
projector_button = button.Button(600, 250, projector_img_off, 0.5)

# Extra Buttons - ON
apriltags_button_on = button.Button(720, 100, button_on, 0.5)
tof_button_on = button.Button(720, 175, button_on, 0.5)
projector_button_on = button.Button(720, 250, button_on, 0.5)

# Extra Buttons - OFF
apriltags_button_off = button.Button(770, 100, button_off, 0.5)
tof_button_off = button.Button(770, 175, button_off, 0.5)
projector_button_off = button.Button(770, 250, button_off, 0.5)

# If the extra buttons are on or off. by default, they are off
apriltags = False
tof = False
projector = False

run = True

# Header details
pygame.font.init()
font = pygame.font.Font(None, 20)
header_font = pygame.font.Font(None, 40)
DARK_BLUE = (16, 37, 66)

def draw_header():
    text_surface = header_font.render("BLIMP", True, DARK_BLUE)
    text_rectangle = text_surface.get_rect(center=(435,30))
    screen.blit(text_surface, text_rectangle)

try:
    while run:

        screen.fill((202, 228, 241))
        draw_header()

        # -------------------- IF MODE BUTTONS ARE PRESSED --------------------
        if manual_button.draw(screen):
            # print('MANUAL')
            manual_button = button.Button(100, 400, manual_img_on, 0.5)
            waypoint_button = button.Button(200, 400, waypoint_img_off, 0.5)
            auto_button = button.Button(300, 400, auto_img_off, 0.5)
        if waypoint_button.draw(screen):
            # print('WAYPOINT')
            manual_button = button.Button(100, 400, manual_img_off, 0.5)
            waypoint_button = button.Button(200, 400, waypoint_img_on, 0.5)
            auto_button = button.Button(300, 400, auto_img_off, 0.5)
        if auto_button.draw(screen):
            # print('AUTO')
            manual_button = button.Button(100, 400, manual_img_off, 0.5)
            waypoint_button = button.Button(200, 400, waypoint_img_off, 0.5)
            auto_button = button.Button(300, 400, auto_img_on, 0.5)

        # -------------------- IF EXTRA BUTTONS ARE PRESSED --------------------
        if apriltags_button.draw(screen):
            # print('APRIL TAGS')
            continue
        if tof_button.draw(screen):
            # print('TIME OF FLIGHT SENSORS')
            continue
        if projector_button.draw(screen):
            # print('PROJECTOR')
            continue

        # -------------------- IF EXTRA ON BUTTONS ARE PRESSED --------------------
        if apriltags_button_on.draw(screen):
            if apriltags == False:
                apriltags = True
                print('APRIL TAGS ON')
                apriltags_button = button.Button(600, 100, apriltags_img_on, 0.5)
        if tof_button_on.draw(screen):
            if tof == False:
                tof = True
                print('TIME OF FLIGHT SENSORS ON')
                tof_button = button.Button(600, 175, tof_img_on, 0.5)
        if projector_button_on.draw(screen):
            if projector == False:
                projector = True
                print('PROJECTOR ON')
                projector_button = button.Button(600, 250, projector_img_on, 0.5)
                red.ChangeDutyCycle(20)
                green.ChangeDutyCycle(20)
                blue.ChangeDutyCycle(20)

        # -------------------- IF EXTRA OFF BUTTONS ARE PRESSED --------------------
        if apriltags_button_off.draw(screen):
            # print('APRIL TAGS OFF')
            if apriltags == True:
                apriltags = False
                print('APRIL TAGS OFF')
                apriltags_button = button.Button(600, 100, apriltags_img_off, 0.5)
        if tof_button_off.draw(screen):
            # print('TIME OF FLIGHT SENSORS OFF')
            if tof == True:
                tof = False
                print('TIME OF FLIGHT SENSORS OFF')
                tof_button = button.Button(600, 175, tof_img_off, 0.5)
        if projector_button_off.draw(screen):
            # print('PROJECTOR OFF')
            if projector == True:
                projector = False
                print('PROJECTOR OFF')
                projector_button = button.Button(600, 250, projector_img_off, 0.5)
                red.ChangeDutyCycle(0)
                green.ChangeDutyCycle(0)
                blue.ChangeDutyCycle(0)
        
        # -------------------- IF ARROW BUTTONS ARE PRESSED --------------------
        if left_arrow.draw(screen):
            top.ChangeDutyCycle(0)
            left.ChangeDutyCycle(0)
            right.ChangeDutyCycle(0)
            print('LEFT')
            left.ChangeDutyCycle(10)
        if right_arrow.draw(screen):
            top.ChangeDutyCycle(0)
            left.ChangeDutyCycle(0)
            right.ChangeDutyCycle(0)
            print('RIGHT')
            right.ChangeDutyCycle(10)
        if forward_arrow.draw(screen):
            top.ChangeDutyCycle(0)
            left.ChangeDutyCycle(0)
            right.ChangeDutyCycle(0)
            print('FORWARD')
            left.ChangeDutyCycle(10)
            right.ChangeDutyCycle(10)
        if up_arrow.draw(screen):
            top.ChangeDutyCycle(0)
            left.ChangeDutyCycle(0)
            right.ChangeDutyCycle(0)
            print('UP')
            top.ChangeDutyCycle(20)
        if down_arrow.draw(screen):
            top.ChangeDutyCycle(0)
            left.ChangeDutyCycle(0)
            right.ChangeDutyCycle(0)
            print('DOWN')
            top.ChangeDutyCycle(5)
        
        # -------------------- IF EXIT BUTTON IS PRESSED --------------------
        if exit_button.draw(screen):
            raise Exception("EXIT")

        # Event Handler
        for event in pygame.event.get():
            # Quit game
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

except KeyboardInterrupt:
    print("CLEANUP")
    top.stop()
    left.stop()
    right.stop()
    GPIO.cleanup()
    pygame.quit()