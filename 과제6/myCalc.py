class Calc:
    def __init__(self, x=0):
        self.__data = x

    def setvalue(self, x):
        self.__data = x

    def add(self, x):
        self.__data = self.__data + x
        return self.__data

    def minus(self, x):
        self.__data = self.__data - x
        return self.__data

    def getvalue(self):
        return self.__data
    
    def print(self):
        print(self.__data)


cal1 = Calc()
cal2 = Calc(5)
cal1.setvalue(10)
cal1.add(20)
cal1.minus(5)       #cal1 = 25
cal1.print()
cal2.add(cal1.getvalue())
cal2.print()

