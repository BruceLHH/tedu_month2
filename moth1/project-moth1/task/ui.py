import bll,model,inputint

class StudentManagerView:
    def __init__(self):
        self.__manager = bll.StudentManagerControll()
        self.__input_int = inputint.InputInt()
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
        score = self.__input_int.rightwrite("score")
        age = self.__input_int.rightwrite("age")
        id = self.__input_int.rightwrite("id")
        sex = input("Please input sex: ")
        if id == "":
            id = 0
        else:
            id = int(id)
        stu = model.StudentModel(name, score, sex, age, id)
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

