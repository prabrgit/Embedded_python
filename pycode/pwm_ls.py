from syspwm import SysPWM
from time import sleep
import sys,os
import atexit

slee = 0.02
paus = 20
freq = 0.5*10**3
ducy = 30

pwm = SysPWM(0)
pwm.set_frequency(freq)
pwm.set_duty_cycle(ducy)
atexit.register(pwm.disable)
pwm.enable()
sleep(paus)
