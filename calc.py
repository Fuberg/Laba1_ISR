class Calculator(object):

    def __init__(self, firstNumber, secondNumber):
        # Constructor 
        self.firstNumber = firstNumber
        self.secondNumber = secondNumber

    def plus(self):
        return self.firstNumber + self.secondNumber

    def minusone(self):
        return self.firstNumber - self.secondNumber
        
    def devision(self):
        if self.firstNumber != 0 and self.secondNumber !=0:
            return self.firstNumber / self.secondNumber
        else:
            print("Делить на ноль нельзя !")
            return 0

    def multiply(self):
        return self.firstNumber * self.secondNumber

    # def calculate(self):


class dataHandler():

    def __init__(self, x, y, sign):
        self.x = x
        self.y = y
        self.sign = sign
        self.myCalc = Calculator(self.x, self.y)

    def handler(self):
        if self.sign == "+":
            return "Ответ : " + str(self.myCalc.plus())
        elif self.sign == "-":
            return "Ответ : " + str(self.myCalc.minusone())
        elif self.sign == "/":
            return "Ответ : " + str(self.myCalc.devision())
        elif self.sign == "*":
            return "Ответ : " + str(self.myCalc.multiply())

class binaryHandler():

    def __init__(self):
        self.x10 = int(input("Введите целое десятичное число, которое хотите перевести: "))
        self.xcount = int(input("Введите в какую систему счисления хотите перевести число (2,8,16): "))
    
    def handler(self):
        if self.xcount == 2:
            return "Ответ : " + str(self.binaryConvert())
        elif self.xcount == 8:
            return "Ответ : " + str(self.octConvert())
        elif self.xcount == 16:
            return "Ответ : " + str(self.hexConvert())


    def binaryConvert(self):
        answer = bin(self.x10)
        return answer[2:]

    def octConvert(self):
        answer = oct(self.x10)
        return answer[2:]

    def hexConvert(self):
        answer = hex(self.x10)
        return answer[2:]

def getData():
    x = float(input("Введите первое число: "))
    y = float(input("Введите второе число: "))
    sign = input("Выберите действие ( +, -, /, *) : ")
    return x, y, sign

if __name__ == "__main__":
    answer = input("Вы хотите воспользоваться калькулятором? (да, нет): ")
    if answer == "да":
        tup = getData()
        bla = dataHandler(tup[0], tup[1], tup[2])
        print(bla.handler())
    elif answer == "нет":
        bla = binaryHandler()
        print(bla.handler())

    
    



    
