class A:
    def __init__(self,args):
        self.__p = args

    def showA(self):
        print("self.__p=",self.__p)

a=A(100)
print(a.__p)