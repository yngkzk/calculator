import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

from calc_main_window import CalculatorMainWindow

from calc_view import CalculatorView
from calc_model import SimpleCalcModel


from accounting_calc_view import AccountingCalculatorView
from accounting_calc_model import AccountCalcModel

from calc_control import CalcControlWidget

options = {
    "Simple": {"model": SimpleCalcModel, "view": CalculatorView}, 
    "Account": {"model": AccountCalcModel, "view": AccountingCalculatorView}
}


def switch_mode(name):
    if name in options: 
        model = options[name]["model"]() 
        view = options[name]["view"]() 
        view.set_model(model)
        window.set_view(view)
        window.setFixedSize(view.width, view.height)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorMainWindow("Calculator")

    switch_mode("Simple")

    window.setFont(QFont("Times", 12))

    with open("style.css", "r") as file_sheet:
        app.setStyleSheet(file_sheet.read())

    switch = CalcControlWidget(tuple(options.keys()))
    switch.switched.connect(switch_mode)
    window.set_switch(switch)

    window.show()
    app.exec()
