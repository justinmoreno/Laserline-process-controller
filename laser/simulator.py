"""Laser simulator for offline testing."""


class LaserSimulator:
    def __init__(self):
        self.power = 0
        self.active = False

    def set_power(self, power):
        self.power = power

    def enable(self):
        self.active = True

    def disable(self):
        self.active = False

    def read_power(self):
        return self.power if self.active else 0
