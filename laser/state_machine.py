"""Laser state machine for managing laser modes."""


class LaserStateMachine:
    def __init__(self):
        self.status = "idle"

    def reset(self):
        self.status = "idle"

    def start(self):
        self.status = "running"

    def stop(self):
        self.status = "stopped"
