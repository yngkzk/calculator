from PyQt6.QtWidgets import *

class CalcControlWidget(QWidget):

    def calc_mode_switch(self):
        radiobutton = self.sender()
        if radiobutton.isChecked():
            print(radiobutton)

    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        simple = QRadioButton('Simple')
        simple.setChecked(True)
        simple.toggled.connect(self.calc_mode_switch)
        main_layout.addWidget(simple)

        account = QRadioButton('Account')
        account.toggled.connect(self.calc_mode_switch)
        main_layout.addWidget(account)
