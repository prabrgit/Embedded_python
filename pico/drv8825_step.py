import machine
import utime


DIR = machine.Pin(15, machine.Pin.OUT)
STEP = machine.Pin(14, machine.Pin.OUT)
M0 = machine.Pin(2, machine.Pin.OUT)
M1 = machine.Pin(3, machine.Pin.OUT)
M2 = machine.Pin(4, machine.Pin.OUT)

M0.value(True)
M1.value(True)
M2.value(True)


try:
    while True:
        utime.sleep(1.0)
        DIR.value(True)   #DIR.toggle()
        print('CCW')
        
        for x in range(2000):
            STEP.value(True)
            utime.sleep(0.005)
            STEP.value(False)
            utime.sleep(0.005)
            
        utime.sleep(1.0)
        DIR.value(False)   ##DIR.toggle()
        print('CW')
        
        for x in range(2000):
            STEP.value(True)
            utime.sleep(0.005)
            STEP.value(False)
            utime.sleep(0.005)
            
except KeyboardInterrupt:
    print("Interrupt")
    
    
    
    
