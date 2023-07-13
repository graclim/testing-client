# import GPIO package
import RPi.GPIO as GPIO

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

# Setting frequency (frequency of PWM / Hoe long one period is)
freq1 = freq2 = freq3 = freq4 = freq5 = freq6 = 75

# Setting Duty Cycle (The fraction of one period when a system or signal is active in %)
dc1 = dc2 = dc3 = dc4 = dc5 = dc6 = 25

# Create PWM Object
p1 = GPIO.PWM(18, freq1)
p2 = GPIO.PWM(8, freq2)
p3 = GPIO.PWM(40, freq3)
p4 = GPIO.PWM(26, freq4)
p5 = GPIO.PWM(36, freq5)
p6 = GPIO.PWM(32, freq6)

# Start PWM generation of a specified duty cycle
p1.start(dc1)
p2.start(dc2)
p3.start(dc3)
p4.start(dc4)
p5.start(dc5)
p6.start(dc6)

# ChangeDutyCycle(Duty Cycle)
# This function is used to change the Duty Cycle of signal. 
# We have to provide Duty Cycle in the range of 0 - 100 %.

# ChangeFrequency(frequency)
# This function is used to change the frequency (in Hz) of PWM. 