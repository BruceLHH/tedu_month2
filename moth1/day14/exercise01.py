

class Enemy:
    def __init__(self,name,hp,atk,defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def __str__(self):
        return ("name:%s,hp:%d,atk:%d,defense:%d"%(self.name,self.hp,self.atk,self.defense))
    def __repr__(self):
        return 'Enemy("%s",%d,%d,%d)'%(self.name,self.hp,self.atk,self.defense)

e01 = Enemy("xiaow",100,80,2000)
print (e01)
print()
print (str(e01))
print (repr(e01))

e02 = eval(repr(e01))
print (e02)
e02.name = "wwwwww"