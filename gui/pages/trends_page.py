from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QVBoxLayout


class TrendsPage(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Trends"))

        layout.addStretch()
