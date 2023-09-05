from math import *
from calc_model import CalculatorModel


class MathematicalCalcModel(CalculatorModel):
    _display = '0'

    def command(self, key: str):
        if key in ["log", "2√x", "x²", "x^Y", "sin", "cos", "tan", "cot", "|x|", "x!"]:
            if key == "log":
                self._display = list(self._display)
                cut_word = ['l', 'o', 'g', '10', '(']
                for x in range(5):
                    self._display.insert(x, cut_word[x])
                self._display.append(')')
                self._display = ''.join(self._display)

            if key == "2√x":
                self._display = list(self._display)
                cut_word = [')', '*', '*', '0.5']
                for x in range(4):
                    self._display.append(cut_word[x])
                self._display.insert(0, '(')
                self._display = ''.join(self._display)

            if key == "x²":
                self._display = list(self._display)
                cut_word = [')', '*', '*', '2']
                for x in range(4):
                    self._display.append(cut_word[x])
                self._display.insert(0, '(')
                self._display = ''.join(self._display)

            if key == "x^Y":
                pass

            if key == "sin":
                self._display = list(self._display)
                cut_word = ['s', 'i', 'n', '(']
                for x in range(4):
                    self._display.insert(x, cut_word[x])
                self._display.append(')')
                self._display = ''.join(self._display)

            if key == "cos":
                self._display = list(self._display)
                cut_word = ['c', 'o', 's', '(']
                for x in range(4):
                    self._display.insert(x, cut_word[x])
                self._display.append(')')
                self._display = ''.join(self._display)

            if key == "tan":
                self._display = list(self._display)
                cut_word = ['t', 'a', 'n', '(']
                for x in range(4):
                    self._display.insert(x, cut_word[x])
                self._display.append(')')
                self._display = ''.join(self._display)

            if key == "cot":
                self._display = list(self._display)
                cut_word = ['t', 'a', 'n', '(']
                for x in range(4):
                    self._display.insert(x, cut_word[x])
                self._display.append(')')
                self._display = ''.join(self._display)
                result = 1 / float(eval(self._display))
                self._display = str(result)

            if key == "|x|":
                pass

            if key == "x!":
                pass

        else:
            super(MathematicalCalcModel, self).command(key)


if __name__ == '__main__':
    print('Testing model:')
    calc = MathematicalCalcModel()

    calc.command('(')
    calc.command('10')
    calc.command('-')
    calc.command('7')
    calc.command(')')
    calc.command('.')
    calc.command('(')
    calc.command('3')
    calc.command('+')
    calc.command('7')
    calc.command(')')
    calc.command('x²')
    print(calc.get_display())
    calc.command('=')

    print(calc.get_display())
    calc.command('=')
