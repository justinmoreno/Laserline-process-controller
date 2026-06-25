"""EtherNet/IP driver stub."""


class EthernetIPDriver:
    def __init__(self, host=None, port=44818):
        self.host = host
        self.port = port
        self.connected = False

    def connect(self):
        self.connected = True

    def disconnect(self):
        self.connected = False

    def send(self, data):
        if not self.connected:
            raise RuntimeError("EtherNet/IP driver is not connected")
        return True
