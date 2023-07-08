import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.OUT)
while True:
	print ("LED on")
	GPIO.output(12,GPIO.HIGH)
	time.sleep(2)
	print ("LED off")
	GPIO.output(12,GPIO.LOW)
	time.sleep(2)
