 #Creating and instantiating classes
class Employee:
    num_of_employee = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@kpit.com'
        Employee.num_of_employee += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def emailid(self):
        return '{}'.format(self.email)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amt(cls,amt):
        cls.raise_amt = amt

    @classmethod
    def from_string(cls, emp_str):
        first , last, pay = emp_str.split('-')
        return cls(first,last,pay)

    #This method wont be taking dynamic objects like classes as an input arguement
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True 
        
print('\nNumber of Employees before initializing class')
print("Number of Employees {}".format(Employee.num_of_employee))

emp_1 = Employee('Ishan', 'Sharma', 75000)
emp_2 = Employee('Test', 'User', 5000)

import datetime
my_date = datetime.date(2021, 9 , 10)

print(Employee.is_workday(my_date))
