

class Grenades:
    def __init__(self,name):
        self.name = name
    def inference(self,something,hurt_res):
        something.hurt(hurt_res)

# class Something:
#     def __radd__(self, other):
#         pass

class Enemy:
    def hurt(self,result):
        print ("Enemy is",result)

class Player:
    def hurt(self,result):
        print ("I'm",result)

s01 = Enemy()
sl = Grenades("xiaowang")
sl.inference(s01,"dead!")