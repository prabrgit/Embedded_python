#!/usr/bin/env python3
import serial
import time
import RPi.GPIO as GPIO

LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyS0', 9600)
    ser.reset_input_buffer()
    while True:
        ser.write(b"1")
        print('Off')
        line = ser.readline().decode('utf-8').rstrip()
        line = line.split()[3]
        if(line =="1"):
            GPIO.output(LED_PIN, GPIO.LOW)
            

        ser.write(b"2")
        print('On')
        line1 = ser.readline().decode('utf-8').rstrip()
        line1 = line1.split()[3]
        if(line1 =="2"):
            GPIO.output(LED_PIN, GPIO.HIGH)
        #time.sleep(5)
        