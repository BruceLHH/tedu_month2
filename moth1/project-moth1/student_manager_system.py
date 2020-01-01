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
class StudentManagerControll:
    """
    student manager controll, processing logics
    """
    init_id = 1000
    def __init__(self):
        """
        initial student list
        """
        self.__stu_list = []
    # property n.
    @property
    def stu_list(self):
        """

        :return: student list
        """
        return self.__stu_list
    def add_student(self,student_info):
        """
        add a new student.
        :param student_info: without id student
        :return:
        """
        student_info.id = self.__generate_id()
        self.stu_list.append(student_info)
        #or self.__stu_list.appoed(student_info)
    def __generate_id(self):
        """
        generate student id
        :param student_info:
        :return: None
        """
        StudentManagerControll.init_id += 1
        return StudentManagerControll.init_id
    def remove_student(self,id):
        """
        remove student the repeat id.
        :param id:
        :return:
        """
        for index in range(len(self.stu_list)-1,-1,-1):
            if id == self.stu_list[index].id:
                del self.stu_list[index]
                return True
        return False
    def updata_student_info(self,student):
        """
        updat the student infomation
        :param id:
        :param name:
        :param score:
        :return:
        """
        for item in self.__stu_list:
            if student.id == item.id:
                item.name = student.name
                item.score = student.score
                item.sex = student.sex
                return True
        return False
    def sort_ascending(self):
        for i in range(len(self.stu_list)-1):
            temp = i
            for j in range(i+1,len(self.stu_list)):
                if self.stu_list[j].score<self.stu_list[temp].score:
                    temp = j
            if (i != temp):
                self.stu_list[i],self.stu_list[temp]=self.stu_list[temp],self.stu_list[i]


class StudentManagerView:
    def __init__(self):
        self.__manager = StudentManagerControll()

    def __display_menu(self):
        print ("1) add student infomation:")
        print ("2) display student infomation:")
        print ("3) remove student info:")
        print ("4) updata student info:")
        print ("5) sort student score by ascending:")
    def __select_menu(self):
        value = int(input("Please input:"))
        if value == 1:
            self.__add_stu_info()
        elif value ==2:
            self.__display_info()
        elif value ==3:
            self.__remove_stu_info()
        elif value ==4:
            self.__updata_stu_info()
        elif value ==5:
            self.__sort_ascending_score()
        else:
            return
    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()
    def __add_stu_info(self):
        stu = self.__get_stu_info()
        self.__manager.add_student(stu)

    def __get_stu_info(self):
        name = input("Please the student's name: ")
        score = int(input("Please input score: "))
        age = int(input("Please input age: "))
        sex = input("Please input sex: ")
        id = input("Please input id:")
        if id == "":
            id = 0
        else:
            id = int(id)
        stu = StudentModel(name, score, sex, age, id)
        return stu

    def __display_info(self):
        for item in self.__manager.stu_list:
            print(item.id,item.name,item.sex,item.score,item.age)
    def __remove_stu_info(self):
        id = input("please input the ID you want to delete:")
        id = int(id)
        self.__manager.remove_student(id)
    def __updata_stu_info(self):
        student = self.__get_stu_info()
        if self.__manager.updata_student_info(student):
            print("modify success!")
        else:
            print("modify fail.")
    def __sort_ascending_score(self):
        self.__manager.sort_ascending()


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
view = StudentManagerView()
view.main()