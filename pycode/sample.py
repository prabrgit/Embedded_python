import socket
import time
import pyvisa


class USBScope(object):
    """
    configure oscilloscope through usb
    """

    def __init__(self):
        self.scope = None
        self.resource_manager = pyvisa.ResourceManager()

    def list_usb_devices(self):
        return self.resource_manager.list_resources()

    def connect_usb_scope(self, usb_addr):
        """
        :param host: host address eg. 'USB0::1689::964::C013124::0::INSTR'
        :return: None
        """
        self.scope = self.resource_manager.open_resource(usb_addr)
        

    def write(self, cmd):
        self.scope.write(cmd)

    def query(self, cmd):
        return self.scope.query(cmd)

    def read(self):
        return self.scope.read_raw()

    def close(self):
        self.scope.close()

scope = USBScope()
print(scope.list_usb_devices())
scope.connect_usb_scope(u'ASRL/dev/ttyAMA0::INSTR')

print(scope.query('*IDN?'))
