

class Compute_staff_salary:
    def __init__(self):
        self.all_employees =[]
    def add_staff(self,staff):
        self.all_employees.append(staff)
    def stastic_salary(self):
        res = 0
        for item in self.all_employees:
            res += item.compute_salary()
        return res

class Staff:
    def __init__(self,base_salary):
        self.base_salary = base_salary
    def compute_salary(self):
        return self.base_salary

class Programmer(Staff):
    def __init__(self,base_salary,bonus):
        super().__init__(base_salary)
        self.bonus = bonus
    def compute_salary(self):
        return self.base_salary + self.bonus
class Saler(Staff):
    def __init__(self,base_salary,sale):
        super().__init__(base_salary)
        self.sale = sale
    def compute_salary(self):
        return self.base_salary + self.sale *.05

staff01 = Programmer(3000,400)
staff02 =Saler(4000,80000)
ele = Compute_staff_salary()
ele.add_staff(staff01)
ele.add_staff(staff02)
print (ele.stastic_salary())
