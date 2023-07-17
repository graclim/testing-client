# import GPIO package
import RPi.GPIO as GPIO

# import Time package
from time import sleep

# Numbers the pins from 1-40, starting from the top left then going down to the bottom right
GPIO.setmode(GPIO.BOARD)

# Disable warnings
GPIO.setwarnings(False)

# Setting up the GPIO pins
GPIO.setup(18, GPIO.OUT) # PWM1 Top Motor
GPIO.setup(8, GPIO.OUT)  # PWM2 Left Motor
GPIO.setup(40, GPIO.OUT) # PWM3 Right Motor
GPIO.setup(26, GPIO.OUT) # LED Blue
GPIO.setup(36, GPIO.OUT) # LED Green
GPIO.setup(32, GPIO.OUT) # LED Red

# Setting frequency (frequency of PWM / How long one period is)
topFreq = leftFreq = rightFreq = blueFreq = greenFreq = redFreq = 1000

# Setting Duty Cycle (The fraction of one period when a system or signal is active in %)
topDC = 10
leftDC = 10
rightDC = 10
blueDC = 50
greenDC = 5
redDC = 50

# Create PWM Object
top = GPIO.PWM(18, topFreq)
left = GPIO.PWM(8, leftFreq)
right= GPIO.PWM(40, rightFreq)
blue = GPIO.PWM(26, blueFreq)
green = GPIO.PWM(36, greenFreq)
red = GPIO.PWM(32, redFreq)

# Start PWM generation of a specified duty cycle
top.start(0)
left.start(0)
right.start(0)
blue.start(0)
green.start(0)
red.start(0)

# ChangeDutyCycle(Duty Cycle)
# This function is used to change the Duty Cycle of signal. 
# We have to provide Duty Cycle in the range of 0 - 100 %.

# ChangeFrequency(frequency)
# This function is used to change the frequency (in Hz) of PWM. 

print("Starting motor sequence ...")

try:
    while True:
        top.ChangeDutyCycle(topDC)
        sleep(0.5)
        top.ChangeDutyCycle(0)
        sleep(0.5)

        left.ChangeDutyCycle(leftDC)
        sleep(0.5)
        left.ChangeDutyCycle(0)
        sleep(0.5)

        right.ChangeDutyCycle(rightDC)
        sleep(0.5)
        right.ChangeDutyCycle(0)
        sleep(0.5)

        blue.ChangeDutyCycle(blueDC)
        sleep(0.5)
        blue.ChangeDutyCycle(0)
        sleep(0.5)

        green.ChangeDutyCycle(greenDC)
        sleep(0.5)
        green.ChangeDutyCycle(0)
        sleep(0.5)

        red.ChangeDutyCycle(redDC)
        sleep(0.5)
        red.ChangeDutyCycle(0)
        sleep(0.5)

except KeyboardInterrupt:
    top.stop()
    left.stop()
    right.stop()
    blue.stop()
    green.stop()
    red.stop()
    GPIO.cleanup()
    quit()