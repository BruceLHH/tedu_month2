"""

"""
class Master:
    def __init__(self,master,kongfu):
        self.master = master
        self.kongfu = kongfu
    @property
    def master(self):
        return self.__master
    @master.setter
    def master(self,teacher):
        self.__master = teacher

    @property
    def kongfu(self):
        return self.__kongfu
    @kongfu.setter
    def kongfu(self, kongfu):
        self.__kongfu = kongfu

class Apprentice:
    def __init__(self,apprentice,kongfu):
        self.apprentice = apprentice
        self.kongfu = kongfu
    @property
    def apprentice(self):
        return self.__apprentice
    @apprentice.setter
    def apprentice(self,tudi):
        self.__apprentice = tudi

    @property
    def kongfu(self):
        return self.__kongfu

    @kongfu.setter
    def kongfu(self, kongfu):
        self.__kongfu = kongfu
    def teach(self,master):
        if self.kongfu == master.kongfu:
            print ("I was obtained the kongfu")
        else:
            self.kongfu = master.kongfu
            print (master.master,"teach",self.apprentice,master.kongfu)
master = Master("zhanguwuji","9 sun shen gong")
apprentice = Apprentice("zhaoming",None)
apprentice.teach(master)

master = Master("zhaoming","make-up")
apprentice = Apprentice("zhangwuji","9 sun shen gong")
apprentice.teach(master)


######
# 2.  name active(work)   make_money
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
        self.__money = money

    # work
class Work:
    def __init__(self,work):
        self.work = work
    @property
    def work(self):
        return self.__work
    @work.setter
    def work(self,work):
        self.__work = work
    def earn(self,person):
        print (person.name,"make",self.work,"earn %d"%person.money)

xm = Person("zm",5000)
work = Work("on duty")
work.earn(xm)


# 4.
# player: data:name,hp      be_attacked -->hurt,break_sreen,dead(game_over)
# enemy: data:name,hp,   be_attacked-->be_wounded ,dead
# attack:
class Player:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
    @property  # read
    def hp(self):
        return self.__hp
    @hp.setter  # write
    def hp(self, hp):
        self.__hp = hp
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    def be_attacked(self):
        if self.hp>0:
            print("I'm hurted, broken screen sound!")
        else:
            print ("I'm dead.")
            self.name = None
            self.hp = 0
    def print_info(self):
        if self.name:
            print (self.name,"have %d blood."%self.hp)

class Enemy:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    @property  # read
    def hp(self):
        return self.__hp

    @hp.setter  # write
    def hp(self, hp):
        self.__hp = hp

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
    def be_attacked(self):
        if self.hp > 0:
            print("I'm hurted.oh my God!")
        else:
            print("I'm dead. Aa")
            self.name = None
            self.hp = 0
    def print_info(self):
        if self.name:
            print (self.name,"have %d blood."%self.hp)
class Attack:
    def attack(self,victim):
        victim.hp -= 50
        victim.be_attacked()

player = Player("wuji",130)
enemy = Enemy("xiaoming",115)
attack = Attack()
for i in range(3):
    attack.attack(enemy)
enemy.print_info()



