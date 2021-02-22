class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + '@example.com'

    def fullname(self):
        return f"{self.first} {self.last}"  


# creating instances  
emp_1 = Employee('Corey', 'Schafer', 50000)  
emp_2 = Employee('Govind', 'Patwal', 60000)  


# emp_1.full_name = f"{emp_1.first} {emp_1.last}"
# print(emp_1.full_name)


print(emp_1.first)
print(emp_1.last)
print(emp_1.email)
print(emp_1.pay)
print(emp_1.fullname())

print(emp_2.first)
print(emp_2.last)
print(emp_2.email)
print(emp_2.pay)
print(emp_2.fullname())


print('==================')

print(Employee.fullname(emp_1))
print(emp_1.fullname())
Employee.fullname(emp_1)

########################################################
########################################################


# #creating a class
# class Employee:
#     pass

# # creating instances  
# emp_1 = Employee()  
# emp_2 = Employee()  

# # print the instances
# print(emp_1)
# print(emp_2)

# # instance variavles are variables that are unique to instances of the classes
# # manually creating instance variables ---- ineffective
# emp_1.first = 'Corey'
# emp_1.last = 'Schafer'
# emp_1.email = f"{emp_1.first}.{emp_1.last}@example.com"
# emp_1.pay = 50000

# emp_2.first = 'Govind'
# emp_2.last = 'Patwal'
# emp_2.email = emp_2.first + '.' + emp_2.last + '@example.com'
# emp_2.pay = 50000

# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.email)
# print(emp_1.pay)

# print(emp_2.first)
# print(emp_2.last)
# print(emp_2.email)
# print(emp_2.pay)