#Class methods
#This video is focussed on class variables 

 #First Video 
 #Cory Schaffer 

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
        


print('\nNumber of Employees before initializing class')
print("Number of Employees {}".format(Employee.num_of_employee))

emp_1 = Employee('Ishan', 'Sharma', 75000)
emp_2 = Employee('Test', 'User', 5000)

print(Employee.emailid(emp_2))


#Class is a blueprint to create instances

#Now, as you see the varibale is approachable from both class and instance itself
#
print(emp_1.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employee.__dict__)

emp_1.raise_amount = 1.10
print(emp_1.raise_amount)

#Now see the value 
print("\nAfter the value has been changed in instance , How does it affect overall scenario?")
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

#It returned two, as it was incremented two times. 

print("Number of Employees {}".format(Employee.num_of_employee))

#Class methods as alternative constructors 

emp_1.set_raise_amt(1.2)

#Now check the raise amount value, after it's getting setup by class method
print("\nAfter the value has been changed using class methods , How does it affect overall scenario?")
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


#
emp1_string = 'Ishan-Sharma-70000'
new_emp_1 = Employee.from_string(emp1_string)

print("\nUsing the Class methods")
print(new_emp_1.pay)
print(new_emp_1.email)