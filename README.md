# Laserline Research Controller

A Python application for controlling a Laserline LDM diode laser through a Yaskawa/VIPA System SLIO EtherNet/IP remote I/O station.

The project is intended for research laboratories and provides a modern software interface for operating the laser, integrating the Mergenthaler LPC04/LASCON pyrometer system, automating experiments, and logging process data.

---

## Features

### Current

- EtherNet/IP communication with VIPA 053-1IP01
- Digital input monitoring
- Digital output control
- Analog input monitoring
- Analog output control
- Laser enable
- Shutter control
- Pilot laser
- Laser reset
- Power control
- Live machine status
- Event logging

### Planned

- LASCON integration
- Pyrometer temperature monitoring
- Experiment automation
- Recipe management
- CSV logging
- Live plots
- Safety state machine
- Remote scripting
- Camera integration
- Windows executable

---

## Project skeleton

```
laserline-research-controller/
│
├── README.md
├── LICENSE
├── requirements.txt
├── config.yaml
├── app.py
│
├── gui/
├── drivers/
├── laser/
├── logger/
├── experiments/
├── tests/
└── docs/
```

## Hardware

Current development platform:

- Laserline LDM diode laser
- Yaskawa/VIPA System SLIO
- IM 053-1IP01 EtherNet/IP Adapter
- DI 8x DC24V (021-1BF00)
- DO 8x DC24V (022-1BF00)
- AI 4x 0–10 V (031-1BD30)
- AO 2x 0–10 V (032-1BB30)
- Mergenthaler LPC04
- LASCON Process Manager

---

## Software

- Python 3.12+
- PySide6
- pyqtgraph
- pandas
- numpy
- PyYAML

---

## Architecture

```
Python GUI
      │
EtherNet/IP Scanner
      │
VIPA 053-1IP01
      │
System SLIO
      │
Laserline Customer Interface
      │
Laserline LDM
```

LASCON remains responsible for pyrometer temperature control while the Python application performs machine sequencing, monitoring, logging, and experiment automation.

---

## Project Goals

The software is designed to provide:

- Safe laser operation
- Modular architecture
- Experiment automation
- Repeatable research workflows
- Complete process logging
- Easy future expansion

---

## Project Status

🚧 Under active development.

Current milestone:

- [ ] GUI
- [ ] EtherNet/IP Driver
- [ ] Laser Control
- [ ] LASCON Integration
- [ ] Experiment Automation

---

## License

MIT License
