import RPi.GPIO as GPIO
import time as time
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
 
pwm = GPIO.PWM(18, 500) # GPIO18, frequency=50Hz
pwm.start(40)
try:
   while True:
     for dc in range(10, 91, 10):
        pwm.ChangeDutyCycle(dc)
        print(dc)
        time.sleep(1)
     for dc in range(90, 10, -10):
        pwm.ChangeDutyCycle(dc)
        print(dc)
        time.sleep(1)
except KeyboardInterrupt:
   pass
pwm.stop()
GPIO.cleanup()
