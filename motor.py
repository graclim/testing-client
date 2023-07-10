import time 
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17,GPIO.OUT) # left
GPIO.setup(18,GPIO.OUT) # right
GPIO.setup(22,GPIO.OUT) # top

print('Starting motor sequence!')

while True:
  try:
    # Makes the motor spin one way for 3 seconds
    GPIO.output(17, True)
    GPIO.output(18, False)
    time.sleep(3)
    # Spins the other way for a further 3 seconds
    GPIO.output(17, False)
    GPIO.output(18, True)
    time.sleep(3)
  except(KeyboardInterrupt):
    GPIO.output(17, False)
    GPIO.output(18, False)
    GPIO.cleanup()
    quit()