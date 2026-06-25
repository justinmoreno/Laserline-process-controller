# Laser Operation

This document explains the laser operation sequence and state transitions.

- `OFF` -> `READY`
- `READY` -> `THRESHOLD`
- `THRESHOLD` -> `SHUTTER`
- `SHUTTER` -> `RUNNING`

Shutdown returns the system to `READY`.
