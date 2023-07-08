import binascii
import threading
import time

import serial
from serial.tools.list_ports import comports


class SerialCom:
    def __init__(self):
        self.serial = serial.Serial()

    def open_port(self, port):
        self.serial.open()

    @staticmethod
    def list_port():
        result = []
        for (port, name, hwid) in sorted(comports()):
            result.append([str(port), str(name), str(hwid)])
            # print 'PORT :', port, ' NAME :', name, '\n'
        return result

    @staticmethod
    def get_port(usb_name):
        for (port, name, hwid) in sorted(comports()):
            if usb_name in name:
                return port

    def close_port(self):
        self.serial.close()

    def write(self, command):
        self.serial.write(command.encode())
        # self.serial.write(bytes("{0}".format(command), encoding='ascii'))

    def query(self, command, timeout=1):
        self.write(command)
        return self.read(timeout)

    def read(self, timeout=1):
        self.serial.timeout = timeout
        data = []
        temp_timeout = self.serial.timeout
        self.serial.timeout = 1
        while 1:
            temp = self.serial.read(1).decode('utf-8')
            # print(temp)
            if temp == '':
                break
            data.append(temp)
        self.serial.timeout = temp_timeout
        return ''.join(data)

    def __del__(self):
        self.close_port()


DATA = []

COLLECTED_DATA = False


def hex_to_dec(hex_data: list[str]) -> int:
    temp = [24, 16, 8, 0]
    res = 0
    for x, y in zip(hex_data, temp):
        res |= int(x, 16) << y
    bits = 32
    if (res & (1 << (bits - 1))) != 0:
        res = res - (1 << bits)
    return res


def collect_data():
    global DATA, obj, COLLECTED_DATA
    DATA = []
    COLLECTED_DATA = False
    while 1:
        temp = obj.serial.read(1)
        if temp == b'':
            break
        # if flag and len(data) > 1000:
        #
        #     flag = False
        DATA.append(temp)
    COLLECTED_DATA = True


obj = SerialCom()
obj.serial.baudrate = 230400
obj.serial.port = "/dev/ttyUSB0"
obj.serial.timeout = 5
obj.serial.open()
obj.serial.write(bytearray([0x08, 0x01, 0x00, 0x00, 0x00]))
proc = threading.Thread(target=collect_data, args=())
proc.start()
time.sleep(1)
obj.serial.write(bytearray([0x08, 0x02, 0x00, 0x00, 0x00]))
time.sleep(0.5)
while 1:
    if COLLECTED_DATA:
        break
print("[ info ] DATA LEN :", len(DATA))
print(DATA)
