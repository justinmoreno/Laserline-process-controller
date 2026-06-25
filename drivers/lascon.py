"""Lascon driver stub."""


class LasconDriver:
    def __init__(self, host=None, port=None):
        self.host = host
        self.port = port
        self.connected = False

    def connect(self):
        self.connected = True

    def disconnect(self):
        self.connected = False

    def send_command(self, command):
        if not self.connected:
            raise RuntimeError("Lascon driver is not connected")
        return True
