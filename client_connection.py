import socket
from time import sleep
import RPi.GPIO as GPIO

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

# RPI 3 Base Station IP Address
host = ''
port = 5580

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

try:

    while True:
        # command = input("Enter your command: ")
        # top.ChangeDutyCycle(0)
        # right.ChangeDutyCycle(0)
        # left.ChangeDutyCycle(0)
        # if command == 'EXIT':
        #     s.send(str.encode(command))
        #     break
        # elif command == 'KILL':
        #     s.send(str.encode(command))
        #     break
        # s.send(str.encode(command))
        reply = s.recv(1024)
        reply = reply.decode('utf-8')
        
        if reply == "forward":
            left.ChangeDutyCycle(10)
            right.ChangeDutyCycle(10)
        elif reply == "left":
            left.ChangeDutyCycle(10)
        elif reply == "right":
            right.ChangeDutyCycle(10)
        # elif reply == "up":
        #     top.ChangeDutyCycle(20)
        # elif reply == "down":
        #     top.ChangeDutyCycle(5)
        print(reply)
    
finally:
    top.stop()
    left.stop()
    right.stop()
    GPIO.cleanup()
    s.close()