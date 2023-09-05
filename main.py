import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from calc_main_window import CalculatorMainWindow
from calc_view import CalculatorView
from calc_model import SimpleCalcModel
from mathematical_calc_view import MathematicalCalcView
<<<<<<< Updated upstream
from calc_control import CalcControlWidget


def switch_mode(name):
    if name == 'Account':
        # model = AccountCalcModel()
        # view = AccountCalcView()
        layout.set_model(model)
        main_window.set_view(layout)
=======
from mathematical_calc_model import MathematicalCalcModel
>>>>>>> Stashed changes


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = CalculatorMainWindow("Calculator")
    layout = MathematicalCalcView()
    model = MathematicalCalcModel()

    main_window.setFixedSize(CalculatorView.window_size, CalculatorView.window_size)
    main_window.setFont(QFont("Times", 12))

    switch = CalcControlWidget()
    switch.switched.connect(switch_mode)
    main_window.set_switcher(switch)

    layout.set_model(model)
    main_window.set_view(layout)
    main_window.show()
    app.exec()

#  QWidget.SetFocusPolicy()
#  super().__init__() надо писать в конце (!!), но только с model (!!!)
#  set_model должен быть в calc_main_window
#
