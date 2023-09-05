from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal


class CalcControlWidget(QWidget):
    switched = pyqtSignal(str)

    def calc_mode_switch(self):
        radiobtn = self.sender()
        if radiobtn.isChecked():
            text = radiobtn.text()
            self.switched.emit(text)

    def __init__(self, options):
        super().__init__()

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)


        for i in range(len(options)): 
            radioButton = QRadioButton(text=options[i])
            radioButton.toggled.connect(self.calc_mode_switch)
            main_layout.addWidget(radioButton)
    
            if i == 0: 
                radioButton.setChecked(True)
        

        # simple.move(10, 0)
        # accounting.move(85, 0)
        # mathematical.move(195, 0)