"""
xioaming
"""
class Person:
    def __init__(self,name,money):
        self.name = name
        self.money = money
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self,money):
        self.__money =money

class Bank:
    def __init__(self,position,money):
        self.position = position
        self.money = money

    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, position):
        self.__position = position
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self, money):
        self.__money = money
    def draw_money(self,person,draw_number):
        self.money -= draw_number
        person.money += draw_number
        print ("xiaoming draw %d,the bank leave %d money."%(person.money,self.money))

xm = Person("xiaoming",5)
band = Bank("gonghang",100000)
band.draw_money(xm,5000)
