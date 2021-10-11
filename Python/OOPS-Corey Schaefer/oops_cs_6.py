#Special Methods in Python
class Employee:
    #num_of_employee = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@kpit.com'
        #Employee.num_of_employee += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def emailid(self):
        return '{}'.format(self.email)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
    
    def user_name(self):
        return '{}{}'.format(self.first, self.dum1)
    #return '{} {}'.format(self.first, x)

    #dunder repr and dunder str function

    #Used from the development side by the developer
    def __repr__(self):
        return "Employee('{}' , '{}' , '{}' )".format(self.first,self.last,self.pay)

    #Used by the user side to know, How the o/p would look like 
    def __str__(self):
        return '{} -{}'.format(self.fullname(), self.email)


emp_1 = Employee('Ishan', 'Sandex', 95000)

""""
print(repr(emp_1))
print(str(emp_1))
"""

print(emp_1.__repr__())
print(emp_1.__str__())