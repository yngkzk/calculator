from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from calc_view import CalculatorView


class AccountingCalculatorView(CalculatorView):

    keyBoard = [
            ["MC", "MR", "M+", "M-", "%"],
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="],
    ]

    def __init__(self):  
        super().__init__()
        
        self.create_buttons(self.keyBoard)

         



