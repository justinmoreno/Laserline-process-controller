from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QVBoxLayout


class ControlPage(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Laser Control"))

        layout.addStretch()
