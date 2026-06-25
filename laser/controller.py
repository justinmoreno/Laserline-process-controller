from enum import Enum, auto


class LaserState(Enum):
    OFF = auto()
    READY = auto()
    THRESHOLD = auto()
    SHUTTER = auto()
    LASER = auto()
    RUNNING = auto()
    FAULT = auto()


class LaserController:

    def __init__(self):

        self.state = LaserState.OFF

        self.threshold = False
        self.shutter = False
        self.laser = False

        self.power = 0.0

    def reset(self):

        self.state = LaserState.READY

    def threshold_on(self):

        if self.state != LaserState.READY:
            return

        self.threshold = True
        self.state = LaserState.THRESHOLD

    def shutter_open(self):

        if self.state != LaserState.THRESHOLD:
            return

        self.shutter = True
        self.state = LaserState.SHUTTER

    def laser_on(self):

        if self.state != LaserState.SHUTTER:
            return

        self.laser = True
        self.state = LaserState.RUNNING

    def shutdown(self):

        self.laser = False
        self.shutter = False
        self.threshold = False

        self.state = LaserState.READY

    def set_power(self, percent):

        self.power = max(0, min(percent, 100))
