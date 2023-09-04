import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from calc_main_window import CalculatorMainWindow
from calc_view import CalculatorView
from calc_model import SimpleCalcModel
from mathematical_calc_view import MathematicalCalcView


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = CalculatorMainWindow("Calculator")
    layout = MathematicalCalcView()
    model = SimpleCalcModel()

    layout.set_model(model)
    main_window.setFixedSize(CalculatorView.window_size, CalculatorView.window_size)
    main_window.setFont(QFont("Times", 12))

    main_window.set_view(layout)
    main_window.show()
    app.exec()

#  QWidget.SetFocusPolicy()
#  super().__init__() надо писать в конце (!!)
