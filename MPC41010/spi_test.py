import spidev
import time
spi = spidev.SpiDev() # create spi object
spi.open(0, 0) # open spi port 0, device (CS) 1
spi.max_speed_hz = 5000
spi.xfer([17,19])
time.sleep(100)
spi.close()
