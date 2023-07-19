# import GPIO package and time
import time 
import RPi.GPIO as GPIO

# Setting GPIO pins to be referred to their BOARD number (1-40)
GPIO.setmode(GPIO.BOARD)

# Disable warnings
GPIO.setwarnings(False)	

# Setting up the GPIO pins
GPIO.setup(18,GPIO.OUT) # top
GPIO.setup(8,GPIO.OUT)  # left
GPIO.setup(40,GPIO.OUT) # right

# Setting frequency (frequency of PWM / Hoe long one period is)
freq1 = freq2 = freq3 = 1000

# Setting Duty Cycle (The fraction of one period when a system or signal is active in %)
# The duty cycle for each motor is then initiated with the defined initial value.
# A value of means the motor is initially off.
dc1 = dc2 = dc3 = 0

# Create PWM Object
top = GPIO.PWM(18,freq1)
left = GPIO.PWM(8,freq2)
right = GPIO.PWM(40,freq3)

top.start(0)
left.start(0)
right.start(0)
	
count = 0 

# Testing forward, stop, right, and left
try:
	
	while True:
		print('time ' + str(count))
		
		if count >= 17:
			count = 0
		
		if count == 1:
			top.ChangeDutyCycle(0)
			left.ChangeDutyCycle(10)
			right.ChangeDutyCycle(0)
			print('left')
		
		elif count == 4:
			top.ChangeDutyCycle(0)
			left.ChangeDutyCycle(0)
			right.ChangeDutyCycle(0)
			print('stop')
		
		elif count == 5:
			top.ChangeDutyCycle(10)
			left.ChangeDutyCycle(0)
			right.ChangeDutyCycle(0)
			print('top')
			
		elif count == 8:
			top.ChangeDutyCycle(0)
			left.ChangeDutyCycle(0)
			right.ChangeDutyCycle(0)
			print('stop')
		
		elif count == 9:
			top.ChangeDutyCycle(0)
			left.ChangeDutyCycle(0)
			right.ChangeDutyCycle(10)
			print('right')
			
		elif count == 12:
			top.ChangeDutyCycle(0)
			left.ChangeDutyCycle(0)
			right.ChangeDutyCycle(0)
			print('stop')
		
		elif count == 13:
			top.ChangeDutyCycle(0)
			left.ChangeDutyCycle(10)
			right.ChangeDutyCycle(10)
			print('forward')
			
		elif count == 16:
			top.ChangeDutyCycle(0)
			left.ChangeDutyCycle(0)
			right.ChangeDutyCycle(0)
			print('stop')
		
		time.sleep(1)	
		count += 1	
		
except KeyboardInterrupt:
	print("Ctl C pressed")
	# Stops the PWM signals to all four motors, and returns the pins to their default states. 
	# This is an important step to avoid potential damage to the GPIO pins.
	top.stop()
	left.stop()
	right.stop()
	GPIO.cleanup()
