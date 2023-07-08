import machine
import utime

cs = machine.Pin(17, machine.Pin.OUT)
spi = machine.SPI(0,
                  baudrate=1000000,
                  polarity=1,
                  phase=1,
                  bits=8,
                  firstbit=machine.SPI.MSB,
                  sck=machine.Pin(18),
                  mosi=machine.Pin(19),
                  miso=machine.Pin(16))

msg = bytearray()
msg.append(0x00 | 0x11)
msg.append(0xFF)

msg1 = bytearray()
msg1.append(0x00 | 0x11)
msg1.append(0x80)

msg2 = bytearray()
msg2.append(0x00 | 0x11)
msg2.append(0x00)
 
# Send out SPI message
cs.value(0)
spi.write(msg)
utime.sleep(2.0)
print('LO R')
cs.value(1)

cs.value(0)
spi.write(msg1)
utime.sleep(2.0)
print('MED R')
cs.value(1)

cs.value(0)
spi.write(msg2)
utime.sleep(2.0)
print('HI R')
cs.value(1)

try:
    while True:
        for i in range(255):
            cs.value(0)
            msg = bytearray()
            msg.append(0x00 | 0x11)
            
            msg.append(i)
            spi.write(msg)
            utime.sleep(0.01)
            cs.value(1)
    
        for i in range(255,0,-1):
            cs.value(0)
            msg = bytearray()
            msg.append(0x00 | 0x11)
            
            msg.append(i)
            spi.write(msg)
            utime.sleep(0.01)
            cs.value(1)
            
except KeyboardInterrupt:
    cs.value(0)
    spi.write(msg2)
    cs.value(1)
    print("Interrupt")
    


