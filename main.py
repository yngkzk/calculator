import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from calc_main_window import CalculatorMainWindow
from calc_view import CalculatorView


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window_size = 300

    main_window = CalculatorMainWindow("Calculator")
    layout = CalculatorView()

    main_window.setFixedSize(window_size, window_size)
    main_window.setFont(QFont("Times", 12))

    main_window.set_view(layout)
    main_window.show()
    app.exec()
