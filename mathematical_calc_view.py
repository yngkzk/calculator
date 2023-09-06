from PyQt6.QtWidgets import *
from calc_view import CalculatorView


class MathematicalCalcView(CalculatorView):
    height = 560
    width = 400

    keyBoard = [
        ["log", "2√x", "x²", "sin", "cos"],
        ["x^Y", "|x|", "x!", "tan", "cot"],
        ["7", "8", "9", "/", "C"],
        ["4", "5", "6", "*", "("],
        ["1", "2", "3", "-", ")"],
        ["0", "00", ".", "+", "="],
    ]

    def __init__(self):
        super().__init__()

        self.create_buttons(self.keyBoard)
