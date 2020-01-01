
class AtkValueError(Exception):
    def __init__(self,message,error_line,atk,error_id):
        super(AtkValueError, self).__init__("value is error.")
        self.message = message
        self.error_line = error_line
        self.atk = atk
        self.error_id = error_id

class Enemy:
    def __init__(self,atk):
        self.atk = atk
    @property
    def atk(self):
        return self.__atk
    @atk.setter
    def atk(self,value):
        if 0<= value <= 100:
            self.__atk = value
        else:
            raise AtkValueError("value error.",21,value,10001)

try:
    e01 = Enemy(204)
except AtkValueError as atk:
    print (atk.error_line)


