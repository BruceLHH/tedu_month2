"""


"""
class Student:
    def __init__(self,name,age,score,sex):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex
    def print_self_info(self):
        #
        print ("name is %s,age is %d,score is %d,sex is %s"%(self.name,self.age,self.score,self.sex))

list01 = [
        Student("xiaowang",32,98,"man"),
        Student("xiaohua",14,97,"girl"),
        Student("mingyue",54,97,"girl"),
        Student("wuji",74,97,"man")
    ]

# 1.
def find_name():
    """
    :return:
    """
    for obj in list01:
        if obj.name == "wuji":
            return obj
stu = find_name()
print (stu.name,stu.score)

# 2.
all_girl = []
def find_all_girl():
    for obj in list01:
        if obj.sex == 'girl':
            all_girl.append(obj)
find_all_girl()
for girl in all_girl:
    print (girl.name,girl.age)

# 3.
def count_age():
    count = 0
    for obj in list01:
        if obj.age >=30:
            count += 1
    return count
print (count_age())

# 4.
def score_to_zero():
    for obj in list01:
        obj.score = 0
score_to_zero()
#test
for obj in list01:
    obj.print_self_info()

# 5.
def get_all_name():
    name = []
    for obj in list01:
        name.append(obj.name)
    return name
print (get_all_name())

# 6.
def find_max_age_obj():
    max_age_stu = list01[0]
    for obj in list01:
        if obj.age>max_age_stu.age:
            max_age_stu = obj
    return max_age_stu
print (find_max_age_obj().age)
