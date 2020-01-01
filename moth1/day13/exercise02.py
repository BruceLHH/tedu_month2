
class Car:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
    def print_info(self):
        print (self.brand,self.speed)

class Diandongche(Car):
    def __init__(self,brand,speed,battery_content,power):
        super().__init__(brand,speed)
        self.battery_content = battery_content
        self.power = power
    def print_info(self):
        print (self.brand,self.speed,self.power)
w01 = Car("xiao",410)
Dian = Diandongche("df41",410,20000,8000)
Dian.print_info()
w01.print_info()
