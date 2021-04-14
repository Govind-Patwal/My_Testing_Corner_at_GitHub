# # '''
# # This Course is one of the main reason I joined this specialization.
# # It provides an intro to Classes and Inheretance.
# # '''

# # # define a class that has the defualt values for x and y

# # # class Point:  
# # #     '''
# # #     Class for representing and manipulating x,y coordinates
# # #     convention is to start the class name with a capital letter
# # #     '''
# # #     def __init__(self): 
# # #         '''
# # #         functions of a class are called methods
# # #         always have at least one variable, it can be anything, self is the default
# # #         self variable refers to the instance of the class

# # #         Every class should have a method with the special name __init__.
# # #         This initializer method also called constructor is automaiically 
# # #         called whenever a new instance of Point is created. It gives the 
# # #         programmer the opportunity to set up the attributes requied with 
# # #         the new instance by giving them their initial state values/attributes.
# # #         The self parameter is automatically set to reference the newly created 
# # #         object that needs to be initialized. for example if the name of the 
# # #         instance is instance1  self.x will be equal to instance1.x ...
# # #         '''
# # #         self.x = 0  # initializing self.x  Or instance.x = 0
# # #         self.y = 0  # initializing self.y  OR instance.y = 0
# # #         self.z = 5

# # # point1 = Point() 
# # # ''' 
# # # instantiate point1 of class Point, since the __init__ says self.x=0 and self.y=0 , this will set
# # # point1.x = 0 and point1.y = 0
# # # '''
# # # point2 = Point()
# # # '''
# # # instantiate point2 of class Point, since the initializer/constructer method __init__ 
# # # mentions self.x =0 and self.y =0, point2.x and point2.y will be set to 0
# # # '''
# # # point3 = Point()

# # # print(point1)
# # # print(point2)
# # # print(point3)

# # # '''
# # # Instantiating = Constructor function + initializing the variables
# # # >>> instance_name = class_name()

# # # constructor function name =  the name of the class
# # # initializing = workin on the __init__ funtion

# # # A constructor function crates a new object instance, by default it is instance_name = class_name()
# # # The definition of the constructor lies within the __init__ function
# # # '''

# # # # defining a class
# # # class Point:
# # #     def __init__ (self):  # initializer or constructor by using dunderscore inti dunderscore
# # #         self.x= 4
# # #         self.y=6

# # # # instantiating
# # # point1 = Point()  
# # # point2 = Point()

# # # print(point1.x)
# # # print(point2.x)

# # ##  adding variables to the constructor

# # # class Point:  # defining the class
# # #     ''' class the represents the coordinates of a point '''
# # #     def __init__ (self, x, y):  
# # #         ''' 
# # #         this is the constructor method/ also called initializer
# # #         x and y here are the constructor arguments
# # #         '''
# # #         self.var1 = x   # var 1 is an instance variable
# # #         self.var2 = y  # var 1 is also an instance variable

# # # point1 = Point(12,23) # instantiating

# # # print(point1.var2)

# # # class Point():
# # #     ''' Point is a class that has the variables as x and y and methods to display
# # #     them '''
# # #     def __init__ (self, x, y):
# # #         ''' constructor method or initializer.
# # #         as with all methods (functions within classes), it always at least 1
# # #         argument, self, which refers to the instance

# # #         x, y are the constructors arguments 

# # #         since there are 2 constructor arguments, any instantition of this class 
# # #         will require 2 variables
# # #         '''

# # #         self.var_x = x  # var_x is an instance variable
# # #         self.var_y = y  # var_x is another instance variable

# # #     def display_x(self):  # this is a method so at least the self arguments is required
# # #         print(self.var_x) # to display the current instance varaible self has to be used

# # #     def display_y(self, z):  # this is a method so at least the self arguments is required
# # #         print(z)
# # #         print(self.var_y) # to display the current instance varaible self has to be used
# # #         print(self.var_y * z)

# # #     def distanceFromOrigin(self):
# # #         self.sum = self.var_x**2 + self.var_y**2
# # #         return self.sum

# # # point1 = Point(12,34)
# # # point2 = Point(23,45)

# # # print(  point1.var_x )
# # # print(  point1.distanceFromOrigin()  )


# # # class City():
# # #     '''class to represent and manipulate citi variables '''

# # #     def __init__ (self, x, y, z):
# # #         self.name = x
# # #         self.population = y
# # #         self.province = z

# # # cityName = ['Toronto', ' Calgary', 'Hamilton', 'Ottawa']
# # # population = [234567, 800909, 80808080, 8080080]
# # # province = ['ON', 'AB', 'ON', 'ON']

# # # city_tuple = zip(cityName, population, province)

# # # list_of_city_instances = [City(x,y,z) for x,y, z in city_tuple ]

# # # print(list_of_city_instances)


# # # we can pass class instances as arguments

# # # class Point():
# # #     ''' class to represent and manipulate x,y coordinates of a point '''
# # #     # constrctor method or initializor
# # #     def __init__ (self, x, y):
# # #         self.x = x 
# # #         self.y = y 

# # #     # __str__ makes the display of the object pretty, it gets returned when print(instance) is executed
# # #     def __str__ (self):
# # #         return 'Point at ({}, {}) .. {}'.format(self.x, self.y, 'gibberesh')

# # #     # defining the distance function as a method
# # #     def half_of_points(self, instance2):
# # #         new_x = (self.x + instance2.x)/2
# # #         new_y = (self.y + instance2.y)/2
# # #         return Point(new_x, new_y)
 
# # #     def __add__ (self, instance2):
# # #         return Point(self.x + instance2.x, self.y + instance2.y)

# # # # instantiating
# # # point1 = Point(12,23)
# # # point2 = Point(78,34)

# # # point3 = point1 + point2
# # # print(point3)

# # # point4 = point1.half_of_points(point2)

# # # print(point4)  

# # # print(point4.x)
# # # print(point4.y)

# # # help(filter)

# # class Fruit():
# #     def __init__ (self, name, price, quantity):
# #         self.name = name
# #         self.price = price
# #         self.quantity = quantity

# #     def __str__ (self):
# #         return '{} is priced as {} and has a quanity of {} in stock'.format(self.name, self.price, self.quantity)

# # fruit_names = ['Apples', 'Pears', 'Bananas', 'Grapes']        
# # fruit_prices = [12,45,1,3]
# # fruit_qty = [100,34,789,12]

# # fruit_tuples = zip(fruit_names, fruit_prices, fruit_qty)

# # fruit_instance_list = [Fruit(n,p,q) for n,p,q in fruit_tuples ]

# # sorted_fruits_on_name = sorted(fruit_instance_list, key = lambda self: self.name, reverse=True)
# # sorted_fruits_on_price = sorted(fruit_instance_list, key = lambda self: self.price)
# # sorted_fruits_on_qty = sorted(fruit_instance_list, key = lambda self: self.quantity)

# # print('\n*** REVERSE sorting instances based on names ***')
# # print( [instance.name  for instance in sorted_fruits_on_name ] )
# # print( [ (instance.name, instance.price, instance.quantity)  for instance in sorted_fruits_on_name ] )

# # print('\n*** sorting instances based on prices ***')
# # print( [instance.price  for instance in sorted_fruits_on_price ] )
# # print( [ (instance.name, instance.price, instance.quantity)  for instance in sorted_fruits_on_price ] ) 

# # print('\n*** sorting instances based on Quantity ***')
# # print( [instance.quantity  for instance in sorted_fruits_on_qty ] )
# # print( [ (instance.name, instance.price, instance.quantity)  for instance in sorted_fruits_on_qty ] ) 


# # GOAL: to create a Class that has 3 instance variables, the values are 
# # stored in 3 different lists, each of length 5, the values are positional
# # create 5 instances of the class and sort the instances according to the 
# # price

# list1 = ['apples', 'oranges', 'peaches', 'carrots', 'papaya']
# list2 = [100, 200, 13, 2, 120]
# list3 = [12.5, 22.3, 25.8, 2.3, 45.56]

# class Class1(): # defining the class
#     '''this class represents and manipulates fruits  
#     '''
#     def __init__ (self, fruit, quantity, price): # constructor
#         self.fruit = fruit
#         self.quantity = quantity
#         self.price = price

#     def __str__ (self): # special function to display instance as a string rather than pointing to its address when printed
#         return '{} has Quantity {} and price {}'.format(self.name, self.quantity, self.price)

# # instantiating 

# instance_list = [ Class1(x,y,z) for x,y,z in zip(list1, list2, list3) ]

# print('*** Sorted list according to names ***')
# print('*** this will print the address of the sorted instances ***')
# print(sorted(instance_list, key=lambda self: self.fruit))

# print('*** this is printing the values as tuples of the sorted list ***')
# print( [ (instance1.fruit, instance1.quantity, instance1.price) for f in sorted(instance_list, key=lambda self: self.fruit)     ] )


import random


print('--------------------')
print(random.random())
print(random.random())
print('--------------------')
print(random.randrange(5,20,3))
print(random.randrange(5,20,3))
print('--------------------')
for i in range(5,20,3):
    print(i)

    
