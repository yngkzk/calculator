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
                self._display = list(self._display)
                cut_word = [')', '*', '*']
                for x in range(3):
                    self._display.append(cut_word[x])
                self._display.insert(0, '(')
                self._display = ''.join(self._display)

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
                self._display = float(eval(self._display))
                number_module = str(self._display).split('.')
                self._display = abs(int(number_module[0]))
                self._display = str(self._display)
            if key == "x!":
                self._display = float(eval(self._display))
                num = 1
                while self._display >= 1:
                    num = num * self._display
                    self._display = self._display - 1
                float_number = str(num).split('.')
                if float_number[1] == '0':
                    self._display = float_number[0]
                else:
                    self._display = ''.join(float_number)
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
    calc.command('|x|')
    print(calc.get_display())
    calc.command('=')

    print(calc.get_display())
    calc.command('=')
