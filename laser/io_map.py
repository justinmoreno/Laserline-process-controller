"""Laser IO utilities."""


class LaserIO:
    def __init__(self):
        self.input_map = {}
        self.output_map = {}

    def map_input(self, name, address):
        self.input_map[name] = address

    def map_output(self, name, address):
        self.output_map[name] = address

    def get_input_address(self, name):
        return self.input_map.get(name)

    def get_output_address(self, name):
        return self.output_map.get(name)
