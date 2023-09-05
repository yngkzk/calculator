from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal


class CalcControlWidget(QWidget):
    # switched: pyqtSignal = None

    def calc_mode_switch(self):
        pass
    #     radiobutton = self.sender()
    #     if radiobutton.isChecked():
    #         text = radiobutton.text()

    def __init__(self):
        super().__init__()
        # self.switched = pyqtSignal(str)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        simple = QRadioButton('Simple', self)
        accounting = QRadioButton('Accounting', self)
        mathematical = QRadioButton('Mathematical', self)

        simple.setChecked(True)

        simple.toggled.connect(self.calc_mode_switch)
        accounting.toggled.connect(self.calc_mode_switch)
        mathematical.toggled.connect(self.calc_mode_switch)

        simple.move(10, -5)
        accounting.move(75, -5)
        mathematical.move(165, -5)

