from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal


class CalcControlWidget(QWidget):
    switched: pyqtSignal = None

    def calc_mode_switch(self):
        radiobutton = self.sender()
        if radiobutton.isChecked():
            text = radiobutton.text()
            self.switched.emit(text)

    def __init__(self):
        super().__init__()
        self.switched = pyqtSignal(str)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        simple = QRadioButton('Simple')
        simple.setChecked(True)
        simple.toggled.connect(self.calc_mode_switch)
        main_layout.addWidget(simple)

        account = QRadioButton('Account')
        account.toggled.connect(self.calc_mode_switch)
        main_layout.addWidget(account)
