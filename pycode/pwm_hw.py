from syspwm import SysPWM
from time   import sleep
import sys,os
import atexit

SLEE=0.02
PAUS=2
FREQ=100

S=0.65
E=2.30
M=1.40

#pwm0 is GPIO pin 18 is physical pin 12
pwm = SysPWM(0)
pwm.set_frequency(FREQ)
pwm.set_duty_cycle(S)
atexit.register(pwm.disable)
pwm.enable()
sleep(PAUS)

intS = int(S*100)
intE = int(E*100)
while True:
        for i in range(intS,intE):
                pwm.set_duty_cycle(i/100.0)
                #print i-intS
                sleep(SLEE)
        sleep(PAUS)
        for i in range(intE,intS,-1):
                pwm.set_duty_cycle(i/100.0)
                #print i-intS
                sleep(SLEE)
        sleep(PAUS)
