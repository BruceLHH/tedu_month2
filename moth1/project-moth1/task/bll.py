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
