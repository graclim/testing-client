# import GPIO package
import RPi.GPIO as GPIO

# import Time package
import time as sleep

# Numbers the pins from 1-40, starting from the top left then going down to the bottom right
GPIO.setmode(GPIO.BOARD)

# Disable warnings
GPIO.setwarnings(False)	

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

# ChangeDutyCycle(Duty Cycle)
# This function is used to change the Duty Cycle of signal. 
# We have to provide Duty Cycle in the range of 0 - 100 %.

# ChangeFrequency(frequency)
# This function is used to change the frequency (in Hz) of PWM. 

print("Starting LED sequence ...")

try:
    while True:
        red.ChangeDutyCycle(20)
        sleep(0.5)
        red.ChangeDutyCycle(0)
        sleep(0.5)

        green.ChangeDutyCycle(5)
        sleep(0.5)
        green.ChangeDutyCycle(0)
        sleep(0.5)

        blue.ChangeDutyCycle(20)
        sleep(0.5)
        blue.ChangeDutyCycle(0)
        sleep(0.5)

except KeyboardInterrupt:
    print("Keyboard interrupt")

except Exception as e:
    print("Some other error: " + e)

finally:
    blue.stop()
    green.stop()
    red.stop()
    GPIO.cleanup()
    quit()