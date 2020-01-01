

class Sub:
    def __init__(self,x):
        self.x = x

    def __str__(self):
        return "sub is :" + str(self.x)
    def __sub__(self, other):
        return Sub(self.x -other)
    def __rsub__(self, other):
        return Sub(self.x - other)

    # def __
sub = Sub(3)
print (2 -sub)
print (sub-10)

