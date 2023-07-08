import time
import spidev

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 5000

spi.xfer2([17,0x00])
time.sleep(2)
spi.xfer2([17,0x80])
time.sleep(2)
spi.xfer2([17,0xFF])
time.sleep(2)

for j in range(20):
    for i in range(0,256,10):
        spi.xfer2([17,i])
        time.sleep(0.02)
    for i in range(255,-1,-10):
        spi.xfer2([17,i])
        time.sleep(0.02)

spi.close()



