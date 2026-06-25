from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QVBoxLayout


class HomePage(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Laserline Research Controller")

        title.setStyleSheet("""
            font-size:22px;
            font-weight:bold;
        """)

        layout.addWidget(title)

        layout.addWidget(QLabel("Welcome"))

        layout.addStretch()
