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

# Create PWM Object
top = GPIO.PWM(18, 10000)
left = GPIO.PWM(8, 10000)
right = GPIO.PWM(40, 10000)

# Start PWM generation of a specified duty cycle
top.start(0)
left.start(0)
right.start(0)

# ChangeDutyCycle(Duty Cycle)
# This function is used to change the Duty Cycle of signal. 
# We have to provide Duty Cycle in the range of 0 - 100 %.

# ChangeFrequency(frequency)
# This function is used to change the frequency (in Hz) of PWM. 

print("Starting motor sequence ...")

try:
    while True:
        top.ChangeDutyCycle(25)
        sleep(0.5)
        top.ChangeDutyCycle(0)
        sleep(0.5)

        left.ChangeDutyCycle(25)
        sleep(0.5)
        left.ChangeDutyCycle(0)
        sleep(0.5)

        right.ChangeDutyCycle(25)
        sleep(0.5)
        right.ChangeDutyCycle(0)
        sleep(0.5)

except KeyboardInterrupt:
    print("Keyboard interrupt")

except Exception as e:
    print("Some other error: " + e)

finally:
    top.stop()
    left.stop()
    right.stop()
    GPIO.cleanup()
    quit()