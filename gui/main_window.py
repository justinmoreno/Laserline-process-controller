"""Main application window for the Laserline GUI."""
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from .status_panel import StatusPanel
from .control_panel import ControlPanel


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Laserline Process Controller")
        self._setup_ui()

    def _setup_ui(self):
        central = QWidget()
        layout = QVBoxLayout(central)
        self.status_panel = StatusPanel()
        self.control_panel = ControlPanel()
        layout.addWidget(self.status_panel)
        layout.addWidget(self.control_panel)
        self.setCentralWidget(central)

    def update_status(self, status):
        self.status_panel.set_status(status)
