

"""
data model :
logic controller:
view

inherit ,ploymorphism
"""
class Master:
    def __init__(self):
        self.all_area = []
    def get_all_area(self,compute_fun):
        if isinstance(compute_fun.compute_area,Graphic):
            raise ValueError("not sub class.")
        self.all_area.append(compute_fun.compute_area())
        res = 0
        for value in self.all_area:
            res += value
        print(res)

class Graphic:
    def compute_area(self,*args):
        raise NotImplementedError("wrong!")
        pass

class Circle(Graphic):
    def __init__(self,r):
        self.r = r
    def compute_area(self):
        self.res = 3.14 * (self.r**2)
        print ("the circle area is %.2f"%self.res)
        return self.res

class Rectangle(Graphic):
    def __init__(self,high,wide):
        self.high = high
        self.wide = wide
    def compute_area(self):
        self.res = self.high *self.wide
        print ("the rectangle area is %d"%self.res)
        return self.res

class ImageView:
    def __init__(self):
        pass

manager = Master()
image01 = Circle(3)
image02 = Rectangle(2,5)
manager.get_all_area(image01)
manager.get_all_area(image02)

