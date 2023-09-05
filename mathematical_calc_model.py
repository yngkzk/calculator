import re
from math import *


class MathematicalCalcModel:
    __display = '0'

    def calculate(self):
        try:
            result = eval(self.__display)
            self.__display = str(result)
        except SyntaxError:
            self.__display = 'Err...'

    def command(self, key: str):
        if key != "=":
            if key.isdigit():
                if self.__display == "0":
                    self.__display = key
                else:
                    if key == "0" or key == "00":
                        if self.__display[-1] not in "+-*/":
                            if self.__display[-1] == '.':
                                self.__display += key
                            elif int(self.__display[-1]) > 0:
                                self.__display += key
                    else:
                        self.__display += key
            else:
                if key in '()':
                    if self.__display[-1] not in "+-*/":
                        if key == '(':
                            if self.__display == '0':
                                self.__display = key
                            elif self.__display[-1] == '.':
                                self.__display = self.__display[:-1] + "*" + key
                            elif self.__display[-1].isdigit() or self.__display[-1] == ')':
                                self.__display += "*" + key
                            else:
                                self.__display += key
                        elif key == ')':
                            if self.__display[-1] == '(':
                                self.__display += '0' + key
                            if self.__display.count('(') > self.__display.count(')'):
                                self.__display += key
                    else:
                        self.__display += key
                else:
                    if key in ["log", "2√x", "x²", "x^Y", "sin", "cos", "tan", "cot"]:
                        if key == "log":
                            pass

                        if key == "2√x":
                            pass

                        if key == "x²":
                            pass

                        if key == "x^Y":
                            pass

                        if key == "sin":
                            pass

                        if key == "cos":
                            pass

                        if key == "tan":
                            pass

                        if key == "cot":
                            pass
                    else:
                        if self.__display == '0':
                            self.__display = key
                        if key == ".":
                            if "." in self.__display:
                                self.__display = self.__display
                            else:
                                self.__display += key
                        else:
                            self.__display += key

            if key == "C":
                self.__display = "0"

            if key == "log":
                pass

            if key == "2√x":
                pass

            if key == "x²":
                pass

            if key == "x^Y":
                pass

            if key == "sin":
                pass

            if key == "cos":
                pass

            if key == "tan":
                pass

            if key == "cot":
                pass

        else:
            if self.__display.count('(') > self.__display.count(')'):
                self.__display += ')' * int(self.__display.count('(') - self.__display.count(')'))
                index = self.__display.rfind('(')
                numbers = re.split(r'[ +\-*/\().]+', self.__display)
                self.__display = list(self.__display)
                self.__display.insert(index + 1, numbers[-2])
                self.__display = ''.join(self.__display)

            elif self.__display[-1] == '(':
                self.__display = self.__display[:-2]

            elif self.__display[-1] in '+-*/':
                self.__display = self.__display[:-1]
            print(self.__display)
            self.calculate()

    def get_display(self):
        return self.__display


if __name__ == '__main__':
    print('Testing model:')
    calc = MathematicalCalcModel()

    calc.command('(')
    calc.command('9')
    calc.command('-')
    calc.command('7')
    calc.command(')')
    calc.command('.')
    calc.command('(')
    calc.command('3')
    calc.command('+')
    calc.command('4')
    calc.command(')')
    calc.command('(')
    print(calc.get_display())
    calc.command('=')

    print(calc.get_display())
    calc.command('=')
