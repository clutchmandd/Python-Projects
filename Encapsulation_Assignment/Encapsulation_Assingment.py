class Protected:
    def __init__(self):
        self._protectedVar = 35

obj = Protected()
obj._protectedVar = 45
print(obj._protectedVar)

class Protected2:
    def __init__(self):
        self.__privateVar = 33

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Protected2()
obj.getPrivate()
obj.setPrivate(43)
obj.getPrivate()
