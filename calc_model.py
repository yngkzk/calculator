import re
from math import *


class SimpleCalcModel:
    def __init__(self):
        self._display = '0'

    def calculate(self):
        try:
            result = str(eval(self._display, globals()))
            if "." in result and result[-2] == '.' and result[-1] == '0':
                result = result[:-2]
            self._display = result
        except Exception as e:
            print("Некорректное выражение:", e)

    def command(self, key: str):
        if key != "=":
            if key.isdigit():
                if self._display == "0":
                    self._display = key
                else:
                    if key == "0" or key == "00":
                        if self._display[-1] not in "+-*/":
                            if self._display[-1] == '.':
                                self._display += key
                            else:
                                self._display += key
                    else:
                        self._display += key
            else:
                if key in '()':
                    if self._display[-1] not in "+-*/":
                        if key == '(':
                            if self._display == '0':
                                self._display = key
                            elif self._display[-1] == '.':
                                self._display = self._display[:-1] + "*" + key
                            elif self._display[-1].isdigit() or self._display[-1] == ')':
                                self._display += "*" + key
                            else:
                                self._display += key
                        elif key == ')':
                            if self._display[-1] == '(':
                                self._display += '0' + key
                            if self._display.count('(') > self._display.count(')'):
                                self._display += key
                    else:
                        self._display += key
                else:
                    if self._display == '0':
                        self._display = key
                    if key == ".":
                        if "." in self._display:
                            self._display = self._display
                        else:
                            self._display += key
                    else:
                        if self._display[-1] not in "+-*/":
                            self._display += key

            if key == 'AC':
                self._display = self._display[:-3]

            if key == "C":
                self._display = "0"

        else:
            if self._display.count('(') > self._display.count(')'):
                self._display += ')' * int(self._display.count('(') - self._display.count(')'))
                index = self._display.rfind('(')
                numbers = re.split(r'[ +\-*/\().]+', self._display)
                self._display = list(self._display)
                self._display.insert(index + 1, numbers[-2])
                self._display = ''.join(self._display)

            elif self._display[-1] == '(':
                self._display = self._display[:-2]

            elif self._display[-1] in '+-*/':
                self._display = self._display[:-1]
            print(self._display)
            self.calculate()

    def get_display(self):
        return self._display


if __name__ == '__main__':
    print('Testing model:')
    calc = SimpleCalcModel()

    calc.command('3')
    calc.command('+')
    calc.command('+')
    calc.command('7')
    calc.command('.')
    calc.command('2')
    calc.command('-')
    calc.command('5')
    calc.command('=')

    print(calc.get_display())
