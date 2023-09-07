from calc_model import SimpleCalcModel
from math import *


class MathematicalCalcModel(SimpleCalcModel):
    _display = '0'

    def insert_function(self, key):
        is_cot = None
        if key == 'cot':
            key = 'tan'
            is_cot = True
        self._display = list(self._display)
        cut_word = list(key)
        if key == 'log':
            cut_word.append('10')
        cut_word.append('(')
        for x in range(len(cut_word)):
            self._display.insert(x, cut_word[x])
        self._display.append(')')
        self._display = ''.join(self._display)
        if is_cot is True:
            result = 1 / float(eval(self._display, globals()))
            self._display = str(result)
        return self.calculate()

    def insert_expression(self, key):
        self._display = list(self._display)
        cut_word = [')', '*', '*']
        if key == "2√x":
            cut_word.append('0.5')
        if key == "x²":
            cut_word.append('2')
        for x in range(len(cut_word)):
            self._display.append(cut_word[x])
        self._display.insert(0, '(')
        self._display = ''.join(self._display)
        return self._display

    def command(self, key: str):
        if key in ["log", "2√x", "x²", "x^Y", "sin", "cos", "tan", "cot", "|x|", "x!"]:
            if key in ["|x|", "x!"]:
                if key == "|x|":
                    self._display = float(eval(self._display))
                    number_module = str(self._display).split('.')
                    self._display = abs(int(number_module[0]))
                    self._display = str(self._display)

                if key == "x!":
                    self._display = float(eval(self._display))
                    num = 1
                    if self._display < 170:
                        while self._display >= 1:
                            num = num * self._display
                            self._display = self._display - 1
                        float_number = str(num).split('.')
                        self._display = ''.join(float_number)
                    else:
                        self._display = 'Экрана не хватит показать :('
                        self.calculate()

            if key in ["2√x", "x²", "x^Y"]:
                self.insert_expression(key)

            if key in ["log", "sin", "cos", "tan", "cot"]:
                self.insert_function(key)
        else:
            super(MathematicalCalcModel, self).command(key)


if __name__ == '__main__':
    print('Testing model:')
    calc = MathematicalCalcModel()

    calc.command('100')
    calc.command('2√x')
    print(calc.get_display())
    calc.command('=')

    print(calc.get_display())
    calc.command('=')
