

class Grenades:
    def __init__(self,name):
        self.name = name
    def bomb(self,something,hurt_res):
        # duo tai
        something.hurt(hurt_res)

class Something: #father
    # ji cheng
    def hurt(self, hurt_res):
        pass
#####------------------------------------------------
#####------------------------------------------------
class Enemy(Something): # son
    def hurted(self,results):
        print ("Enemy is",results)

class Player(Something):
    def hurted(self,resultss):
        print ("I'm",resultss)

s01 = Enemy()
sl = Grenades("xiaowang")
sl.bomb(s01,"dead!")