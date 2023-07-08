from machine import Pin
import time

led1 = Pin(15, Pin.OUT)
led2 = Pin(0, Pin.OUT)
while True:
    led1.value(1)
    time.sleep(0.05)
    led1.value(0)
    time.sleep(0.05)
    led2.value(1)
    time.sleep(0.1)
    led2.value(0)
    time.sleep(0.1)
