from PyQt6.QtWidgets import *
from calc_view import CalculatorView


class MathematicalCalcView(CalculatorView):
    height = 450
    width = 350

    def __init__(self):
        super().__init__()
        keys_layout = QGridLayout()
        self.layout().addLayout(keys_layout)
        buttonMap = {}
        keyBoard = [
            ["sin", "cos", "log", "x²", "|x|"],
            ["tan", "cot", "2√x", "x^Y", "x!"],
        ]

        for row, keys in enumerate(keyBoard):
            for col, key in enumerate(keys):
                buttonMap[key] = QPushButton(key)
                buttonMap[key].clicked.connect(self.on_button_pressed)
                buttonMap[key].setFixedSize(self.button_width, self.button_height)
                keys_layout.addWidget(buttonMap[key], row, col)
