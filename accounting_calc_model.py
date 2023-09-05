from calc_model import SimpleCalcModel

class AccountCalcModel(SimpleCalcModel): 
    memory = 0 

    def command(self, key: str): 
        if key in "()": 
            self._display += key 
        elif key in "%" and self._display[-1] not in "%":
            self._display += key
        elif key == "M+": 
            self.memory += eval(self._display)
        elif key == "M-": 
            self.memory -= eval(self._display)
        elif key == "MR": 
            self._display = str(self.memory) 
        elif key == "MC": 
            self.memory = 0
        else: 
            super().command(key) 
