# import GPIO package
import RPi.GPIO as GPIO

# import Time package
from time import sleep

# Numbers the pins from 1-40, starting from the top left then going down to the bottom right
GPIO.setmode(GPIO.BOARD)

# Disable warnings
GPIO.setwarnings(False)	

# Setting up the GPIO pins for the motors
GPIO.setup(18, GPIO.OUT) # PWM1 Top Motor
GPIO.setup(8, GPIO.OUT)  # PWM2 Left Motor
GPIO.setup(40, GPIO.OUT) # PWM3 Right Motor

# Setting up the GPIO pins that for some reason have power coming into it
GPIO.setup(7, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)

# Setting GPIO pins not in use to output of 0
GPIO.output(7, 0)
GPIO.output(10, 0)
GPIO.output(24, 0)
GPIO.output(26, 0)
GPIO.output(29, 0)
GPIO.output(31, 0)

# Create PWM Object for motors
top = GPIO.PWM(18, 10000)
left = GPIO.PWM(8, 10000)
right = GPIO.PWM(40, 10000)

# Start PWM generation for motors of a specified duty cycle
top.start(0)
left.start(0)
right.start(0)

# ChangeDutyCycle(Duty Cycle)
# This function is used to change the Duty Cycle of signal. 
# We have to provide Duty Cycle in the range of 0 - 100 %.

# ChangeFrequency(frequency)
# This function is used to change the frequency (in Hz) of PWM. 

# Setting up the GPIO pins for the LEDs
GPIO.setup(26, GPIO.OUT) # LED Blue
GPIO.setup(36, GPIO.OUT) # LED Green
GPIO.setup(32, GPIO.OUT) # LED Red

LEDPinBlue = 26
LEDPinGreen = 36
LEDPinRed = 32

# Create PWM Object for LEDs
blue = GPIO.PWM(LEDPinBlue, 1000)
green = GPIO.PWM(LEDPinGreen, 100)
red = GPIO.PWM(LEDPinRed, 1000)

# Start PWM generation for LEDs of a specified duty cycle
blue.start(0)
green.start(0)
red.start(0)

for i in range(3):
	red.ChangeDutyCycle(20)
	sleep(5)
	red.ChangeDutyCycle(0)
	sleep(3)
	
	green.ChangeDutyCycle(5)
	sleep(5)
	green.ChangeDutyCycle(0)
	sleep(3)

top.stop()
right.stop()
left.stop()
red.stop()
green.stop()
blue.stop()
GPIO.cleanup()
