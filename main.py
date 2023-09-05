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

def swich_mode(name):
    if name in options: 
        model = options[name]["model"]() 
        view = options[name]["view"]() 
        view.set_model(model)
        window.set_view(view)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorMainWindow("Calculator")
    
    window.setFixedSize(CalculatorView.window_size, CalculatorView.window_size)
    window.setFont(QFont("Times", 12))

    # view = CalculatorView() 
    # model = SimpleCalcModel()

    switch = CalcControlWidget(tuple(options.keys()))
    switch.switched.connect(swich_mode)
    window.set_switch(switch)

    # view.set_model(model)
    
    # window.set_view(view)
    window.show()
    app.exec()
