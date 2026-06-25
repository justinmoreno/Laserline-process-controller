"""Machine model definitions."""

from dataclasses import dataclass


@dataclass
class Machine:
    """A simple machine model representation."""
    name: str
    serial_number: str
    firmware_version: str

    def __repr__(self) -> str:
        return (
            f"Machine(name={self.name!r}, serial_number={self.serial_number!r}, "
            f"firmware_version={self.firmware_version!r})"
        )
