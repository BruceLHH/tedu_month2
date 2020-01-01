"""
creat student class
"""

class Students():
    def __init__(self,name=None,age=0,score=0,sex=None):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex
        self.info = []
    def get_student_info(self):
        while True:
            self.name = input("Please input name:")
            if (self.name ==""):
                break
            self.age = int(input("Please input age:"))
            self.score = int(input("Please input score:"))
            self.sex = input("Please input sex:")
            self.info.append([self.name,self.age,self.score,self.sex])
    def print_student_info(self):
        for student_info in self.info:
            print ("the name is %s, age is %d, score is %d, sex is %s"%(student_info[0],
                                                                        student_info[1],
                                                                        student_info[2],
                                                                        student_info[3],
                                                                        ))
    def print_1th_student_info(self):
        print (self.info[0])

obj = Students()
obj.get_student_info()
obj.print_student_info()
obj.print_1th_student_info()