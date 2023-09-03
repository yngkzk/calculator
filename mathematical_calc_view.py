from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class MathematicalCalcView(QWidget):
    calc_model = None
    main_display: QLabel = None

    window_size = 370

    display_height = 50
    button_size = 50

    def on_button_pressed(self):
        btn = self.sender()
        key_text = btn.text()
        self.calc_model.command(key_text)
        self.main_display.setText(self.calc_model.get_display())

    def on_toggled(self):
        hallo = self.sender().text()
        if self.sender().isChecked():
            print(hallo)

    def __init__(self):
        super().__init__()
        mainLayout = QVBoxLayout()

        self.main_display = QLabel(text="0")
        self.main_display.setFixedHeight(self.display_height)
        self.main_display.setFont(QFont('Monospace', 20, QFont.Weight.Normal, False))
        self.main_display.setAlignment(Qt.AlignmentFlag.AlignRight)
        mainLayout.addWidget(self.main_display)

        simple = QRadioButton('Simple', self)
        accounting = QRadioButton('Accounting', self)
        mathematical = QRadioButton('Mathematical', self)
        simple.toggled.connect(self.on_toggled)
        accounting.toggled.connect(self.on_toggled)
        mathematical.toggled.connect(self.on_toggled)
        simple.move(10, 0)
        accounting.move(85, 0)
        mathematical.move(195, 0)

        buttonsLayout = QGridLayout()
        mainLayout.addLayout(buttonsLayout)
        buttonMap = {}
        keyBoard = [
            ["7", "8", "9", "/", "C", "log", "sin"],
            ["4", "5", "6", "*", "(", "2√x", "cos"],
            ["1", "2", "3", "-", ")", "x²", "tan"],
            ["0", "00", ".", "+", "=", "x^Y", "cot"],
        ]

        for row, keys in enumerate(keyBoard):
            for col, key in enumerate(keys):
                buttonMap[key] = QPushButton(key)
                buttonMap[key].clicked.connect(self.on_button_pressed)
                buttonMap[key].setFixedSize(self.button_size, self.button_size)
                buttonsLayout.addWidget(buttonMap[key], row, col)

        self.setLayout(mainLayout)

    def set_model(self, model):
        self.calc_model = model
        self.main_display.setText(self.calc_model.get_display())
