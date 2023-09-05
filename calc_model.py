class SimpleCalcModel:
    def __init__(self):
        self._display = '0'

    def calculate(self):
        try:
            result = eval(self._display)
            self._display = str(result)
        except Exception as e:
            print("Некорректное выражение:", e)

    def command(self, key: str):
        if key.isdigit() or (key == '.' and '.' not in self._display):
            if self._display == "0":
                self._display = key
            else:
                self._display += key
        elif key in "+-*/" and self._display[-1] not in "+-*/":
            self._display += key

        if key == "C":
            if len(self._display) > 1:
                self._display = self._display[:-1]
            else:
                self._display = "0"

        if key == "AC":
            self._display = "0"
        elif key == "=":
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
