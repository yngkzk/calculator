class SimpleCalcModel:
    __display = '0'

    def calculate(self):
        try:
            result = eval(self.__display)
            self.__display = str(result)
        except SyntaxError:
            print("Некоректное выражение")

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
                if self.__display[-1] not in "+-*/":
                    if key == '(':
                        self.__display += "*" + key
                    elif key == ')':
                        if self.__display.count('(') > self.__display.count(')'):
                            self.__display += key
                    else:
                        self.__display += key

            if key == "C":
                if len(self.__display) > 1:
                    self.__display = self.__display[:-1]

            if key == "AC":
                self.__display = "0"

            if key == ".":
                if "." in self.__display:
                    self.__display = self.__display
                else:
                    self.__display += key

        else:
            if '(' in self.__display and ')' not in self.__display:
                self.__display += ')'
            elif self.__display[-1] == '(':
                self.__display = self.__display[:-2]
            print(self.__display)
            self.calculate()

    def get_display(self):
        return self.__display


if __name__ == '__main__':
    print('Testing model:')
    calc = SimpleCalcModel()

    calc.command('3')
    calc.command('+')
    calc.command('7')
    calc.command('00')
    calc.command('.')
    calc.command('0')
    calc.command('5')
    calc.command('(')
    calc.command('23')
    calc.command('+')
    calc.command('52')
    calc.command(')')
    calc.command('(')
    print(calc.get_display())
    calc.command('=')

    print(calc.get_display())
