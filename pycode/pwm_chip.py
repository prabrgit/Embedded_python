import serial
import time

ser = serial.Serial(port='/dev/ttyUSB0',
                    baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1
)


ser.write('S1F100T'.encode())
time.sleep(2)
ser.write('S1D090T'.encode())

'''
for dc in range(10,99,5):
    ser.write(f'S2F050T'.encode())
    time.sleep(10)
    ser.write(f'S2D0{dc}T'.encode())
'''
