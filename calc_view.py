from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class CalculatorView(QWidget):
    calc_model = None
    main_display: QLabel = None

    display_height = 50
    button_size = 50

    text = ""

    def on_button_pressed(self):
        btn = self.sender()
        key_text = btn.text()
        self.calc_model.command(key_text)
        self.main_display.setText(self.calc_model.get_display())
        
    def __init__(self):
        super().__init__()
        mainLayout = QVBoxLayout()

        self.main_display = QLabel(text="0")
        self.main_display.setFixedHeight(self.display_height)
        self.main_display.setFont(QFont('Monospace', 20, QFont.Weight.Normal, False))
        self.main_display.setAlignment(Qt.AlignmentFlag.AlignRight)
        mainLayout.addWidget(self.main_display)

        buttonsLayout = QGridLayout()
        mainLayout.addLayout(buttonsLayout)
        buttonMap = {}
        keyBoard = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="],
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