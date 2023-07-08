import RPi.GPIO as GPIO
from time import sleep

#GPIO.setmode(GPIO.BCM)

# Direction pin from controller
DIR = 40
# Step pin from controller
STEP = 38
# 0/1 used to signify clockwise or counterclockwise.
CW = 1
CCW = 0
#step setting
M0 = 11
M1 = 13
M2 = 15

# Setup pin layout on PI
GPIO.setmode(GPIO.BOARD)

# Establish Pins in software
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

# Set the first direction you want it to spin
GPIO.output(DIR, CW)
try:
	# Run forever.
	while True:

		"""Change Direction: Changing direction requires time to switch. The
		time is dictated by the stepper motor and controller. """
		sleep(1.0)
		# Esablish the direction you want to go
		GPIO.output(DIR,CW)

		# Run for 200 steps. This will change based on how you set you controller
		for x in range(2000):

			# Set one coil winding to high
			GPIO.output(STEP,GPIO.HIGH)
			# Allow it to get there.
			sleep(.005) # Dictates how fast stepper motor will run
			# Set coil winding to low
			GPIO.output(STEP,GPIO.LOW)
			sleep(.005) # Dictates how fast stepper motor will run

		"""Change Direction: Changing direction requires time to switch. The
		time is dictated by the stepper motor and controller. """
		sleep(1.0)
		GPIO.output(DIR,CCW)
		for x in range(2000):
			GPIO.output(STEP,GPIO.HIGH)
			sleep(.005)
			GPIO.output(STEP,GPIO.LOW)
			sleep(.005)

# Once finished clean everything up
except KeyboardInterrupt:
	print("cleanup")
	GPIO.cleanup()
