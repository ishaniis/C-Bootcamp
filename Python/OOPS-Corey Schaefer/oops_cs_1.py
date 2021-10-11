 #First Video 
 #Cory Schaffer 

 #Creating and instantiating classes
class Employee:


#emp_1 = Employee()
#emp_2 = Employee()

#print(emp_1)
#print(emp_2)

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@kpit.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def emailid(self):
        return '{}'.format(self.email)

###
''''''
###
#emp_1.first = 'Ishan'
#emp_1.last = 'Sharma'
#emp_1.pay = '$75k'

#emp_2.first = 'Jayesh'
#emp_2.last = 'Shah'
#emp_2.pay = '$100k'

#print(emp_1.pay)

emp_1 = Employee('Ishan', 'Sharma', '75k')
emp_2 = Employee('Test', 'User', '5k')

print(Employee.emailid(emp_2))


#Class is a blueprint to create instances

