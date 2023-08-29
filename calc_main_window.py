from PyQt6.QtWidgets import QMainWindow


class CalculatorMainWindow(QMainWindow):
    calc_view = None

    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)

    def set_view(self, view):
        self.calc_view = view
        self.setCentralWidget(self.calc_view)
