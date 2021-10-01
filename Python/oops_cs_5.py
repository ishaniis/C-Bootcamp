#Inheritance in the class elements

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

class Developer(Employee):
    raise_amount = 1.50
#Concept of inheritance , Either with super method or Employee method 
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first,last,pay)
        # Other alternative Employee.__init__(self,first, last,pay)
        self.prog_lang = prog_lang

class manager(Employee):

    def __init__(self,first,last,pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

dev_3 = Developer('Cory', 'Schaefer', 50000, 'Python')
#print(dev_3.prog_lang)
#print(dev_3.email)

#dev_2 = Employee('Ishan', 'Sharma', 85000)
dev_1 = Developer('Ishan', 'Sharma', 85000, 'Java')

mgr_1 =  manager('Sue', 'Smith', 90000, [dev_1])
#print(mgr_1.email)

mgr_1.print_emps()

mgr_1.add_emp(dev_3)
print("After adding the employee 3: Corey ")
mgr_1.print_emps()

#Inheritance
print(isinstance(mgr_1, manager))

print(isinstance(mgr_1, Developer))

print(issubclass(manager, Employee))

print(issubclass(manager, Developer))

"""
#print("Salary before the raise is applied ")
#print(dev_1.pay)
print(dev_2.pay)
print("Salary after the raise is applied")
dev_1.apply_raise()
print(dev_1.pay)
print(dev_2.pay)
"""
"""
'{} {}'.format(dev_1.name, dev_1.pay)
'{} {}'.format(dev_2.name, dev_2.pay)
"""

"""

Out of Curiosity  
dev_1 = Developer('Ishan', 'Sharma', 85000)

s = tuple(dev_1.last)
s = s[0]
userid = dev_1.first + s + '@kpit.com'
print(userid)
"""