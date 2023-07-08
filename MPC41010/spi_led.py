import spidev
import time
spi = spidev.SpiDev() # create spi object
spi.open(0, 0) # open spi port 0, device (CS) 1
spi.max_speed_hz = 5000
spi.xfer([17,0xFF])
time.sleep(1)              #to measure resistance, remove PA0 from vcc 
spi.xfer([17,0x80])	   #remove PB0 from Vss, remove LED & resistance
time.sleep(1)		   #get 3 open terminals PB0,PW0 and PA0. Measure
spi.xfer([17,0x00])        #resistance between terminals. 
time.sleep(1)

for j in range(200):
    for i in range(0,256,5):
        spi.xfer([17,i])
        time.sleep(5)
    for i in range(255,-1,-5):
        spi.xfer([17,i])
        time.sleep(5)
    print("Cycle finish")

spi.xfer([17,0x00])
spi.close()


