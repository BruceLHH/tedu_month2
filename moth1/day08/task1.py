"""

creat class
"""

class Man():
    #data members
    def __init__(self,hair,hand=45):
        self.hair = hair
        self.hand = hand

    # members behavior
    def play_boll(self):
        self.res = self.hand**2
        print ("we are together play basketboll with hand. ")
        print (self.hair,self.res)

little_boy = Man("green",34)
member = Man("li",0)
grow = Man('4')
little_boy.play_boll()
member.play_boll()
grow.play_boll()
