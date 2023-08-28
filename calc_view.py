from PyQt5.QtWidgets import *


class SimpleCalcView(QWidget):
    main_display: QLabel = None

    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        main_layout.addWidget(self.main_display)

        # Int buttons

        button1 = QPushButton("1")
        button2 = QPushButton("2")
        button3 = QPushButton("3")
        button4 = QPushButton("4")
        button5 = QPushButton("5")
        button6 = QPushButton("6")
        button7 = QPushButton("7")
        button8 = QPushButton("8")
        button9 = QPushButton("9")
        button0 = QPushButton("0")

        layout = QGridLayout()
        main_layout.addLayout(layout)

        # Int widgets

        layout.addWidget(button1, 3, 0)
        layout.addWidget(button2, 3, 1)
        layout.addWidget(button3, 3, 2)
        layout.addWidget(button4, 2, 0)
        layout.addWidget(button5, 2, 1)
        layout.addWidget(button6, 2, 2)
        layout.addWidget(button7, 1, 0)
        layout.addWidget(button8, 1, 1)
        layout.addWidget(button9, 1, 2)
        layout.addWidget(button0, 4, 1)

        # Math symbols

        button_1 = QPushButton("/")
        button_2 = QPushButton("*")
        button_3 = QPushButton("-")
        button_4 = QPushButton("+")
        button_5 = QPushButton("=")
        button_6 = QPushButton(".")

        # Math widgets

        layout.addWidget(button_1, 1, 3)
        layout.addWidget(button_2, 2, 3)
        layout.addWidget(button_3, 3, 3)
        layout.addWidget(button_4, 4, 3)
        layout.addWidget(button_5, 4, 2)
        layout.addWidget(button_6, 4, 0)
