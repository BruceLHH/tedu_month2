
class Enemy:
    def __init__(self,name,qtk,hp,defense):
        self.set_name(name)
        #self.set_hp(hp)
        self.set_qtk(qtk)
        self.set_defense(defense)
        self.hp = hp

    def set_hp(self,hp):
        if 90< hp <600:
            self.__hp = hp
        else:
            raise ValueError("error!")
    def get_hp(self):
        return self.__hp
    hp = property(get_hp,set_hp)
    def set_name(self,name):
        if name != "":
            self.__name = name
        else:
            raise ValueError("Please input a name.")
    def set_qtk(self,qtk):
        if 100<qtk<=500:
            self.__qtk = qtk
        else:
            raise ValueError("too more.")

    def set_defense(self,defense):
        self.__defense = defense
    ###
    def get_name(self):
        return self.__name
    def get_qtk(self):
        return self.__qtk

    def get_defense(self):
        return self.__defense
    def print_info(self):
        print (self.__name,self.__qtk,self.__hp,self.__defense)

enemy01 = Enemy("huangshang",136,120,98)
enemy01.hp = 500
enemy01.print_info()