"""


"""
class StudentModel:
    """
        student infomation model
    """
    def __init__(self,name="",score=0,sex="",age =0,id = 0):
        """
        create student obj
        :param id:
        :param name:
        :param score:
        :param sex:
        """
        self.id = id
        self.name = name
        self.score = score
        self.sex = sex
        self.age = age
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self,score):
        self.__score = score
    @property
    def sex(self):
        return self.__sex
    @sex.setter
    def sex(self, sex):
        self.__sex = sex



####
"""cont = StudentManagerControll()
stu01 = StudenModel("xiaozhang",23,"man")
stu02 = StudenModel("xiaozhan",24,"man")
upobj = StudenModel("ww",47,"man",1001)

cont.add_student(stu01)
cont.add_student(stu02)
for item in cont.stu_list:
    print (item.name,item.id,item.score)
cont.updata_student_info(upobj)
print()
for item in cont.stu_list:
    print (item.name,item.id,item.score)"""
