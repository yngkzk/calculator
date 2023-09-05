from PyQt6.QtWidgets import QMainWindow, QGridLayout, QWidget


class CalculatorMainWindow(QMainWindow):
    calc_view = None
    calc_layout = None

    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        main_widget = QWidget()
        self.calc_layout = QGridLayout()
        main_widget.setLayout(self.calc_layout)
        self.setCentralWidget(main_widget)

    def set_view(self, view):
        self.calc_view = view
        self.calc_layout.addWidget(self.calc_view, 1, 0)

    def set_switcher(self, widget):
        self.calc_layout.addWidget(widget, 0, 0)

    def set_model(self, model):
        self.calc_model = model
        if self.calc_view:
            self.calc_view.setText(self.calc_model.get_display())
