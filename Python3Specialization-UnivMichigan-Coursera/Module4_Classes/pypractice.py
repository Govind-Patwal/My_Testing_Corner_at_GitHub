# # # # # '''
# # # # # This Course is one of the main reason I joined this specialization.
# # # # # It provides an intro to Classes and Inheretance.
# # # # # '''

# # # # # # define a class that has the defualt values for x and y

# # # # # # class Point:  
# # # # # #     '''
# # # # # #     Class for representing and manipulating x,y coordinates
# # # # # #     convention is to start the class name with a capital letter
# # # # # #     '''
# # # # # #     def __init__(self): 
# # # # # #         '''
# # # # # #         functions of a class are called methods
# # # # # #         always have at least one variable, it can be anything, self is the default
# # # # # #         self variable refers to the instance of the class

# # # # # #         Every class should have a method with the special name __init__.
# # # # # #         This initializer method also called constructor is automaiically 
# # # # # #         called whenever a new instance of Point is created. It gives the 
# # # # # #         programmer the opportunity to set up the attributes requied with 
# # # # # #         the new instance by giving them their initial state values/attributes.
# # # # # #         The self parameter is automatically set to reference the newly created 
# # # # # #         object that needs to be initialized. for example if the name of the 
# # # # # #         instance is instance1  self.x will be equal to instance1.x ...
# # # # # #         '''
# # # # # #         self.x = 0  # initializing self.x  Or instance.x = 0
# # # # # #         self.y = 0  # initializing self.y  OR instance.y = 0
# # # # # #         self.z = 5

# # # # # # point1 = Point() 
# # # # # # ''' 
# # # # # # instantiate point1 of class Point, since the __init__ says self.x=0 and self.y=0 , this will set
# # # # # # point1.x = 0 and point1.y = 0
# # # # # # '''
# # # # # # point2 = Point()
# # # # # # '''
# # # # # # instantiate point2 of class Point, since the initializer/constructer method __init__ 
# # # # # # mentions self.x =0 and self.y =0, point2.x and point2.y will be set to 0
# # # # # # '''
# # # # # # point3 = Point()

# # # # # # print(point1)
# # # # # # print(point2)
# # # # # # print(point3)

# # # # # # '''
# # # # # # Instantiating = Constructor function + initializing the variables
# # # # # # >>> instance_name = class_name()

# # # # # # constructor function name =  the name of the class
# # # # # # initializing = workin on the __init__ funtion

# # # # # # A constructor function crates a new object instance, by default it is instance_name = class_name()
# # # # # # The definition of the constructor lies within the __init__ function
# # # # # # '''

# # # # # # # defining a class
# # # # # # class Point:
# # # # # #     def __init__ (self):  # initializer or constructor by using dunderscore inti dunderscore
# # # # # #         self.x= 4
# # # # # #         self.y=6

# # # # # # # instantiating
# # # # # # point1 = Point()  
# # # # # # point2 = Point()

# # # # # # print(point1.x)
# # # # # # print(point2.x)

# # # # # ##  adding variables to the constructor

# # # # # # class Point:  # defining the class
# # # # # #     ''' class the represents the coordinates of a point '''
# # # # # #     def __init__ (self, x, y):  
# # # # # #         ''' 
# # # # # #         this is the constructor method/ also called initializer
# # # # # #         x and y here are the constructor arguments
# # # # # #         '''
# # # # # #         self.var1 = x   # var 1 is an instance variable
# # # # # #         self.var2 = y  # var 1 is also an instance variable

# # # # # # point1 = Point(12,23) # instantiating

# # # # # # print(point1.var2)

# # # # # # class Point():
# # # # # #     ''' Point is a class that has the variables as x and y and methods to display
# # # # # #     them '''
# # # # # #     def __init__ (self, x, y):
# # # # # #         ''' constructor method or initializer.
# # # # # #         as with all methods (functions within classes), it always at least 1
# # # # # #         argument, self, which refers to the instance

# # # # # #         x, y are the constructors arguments 

# # # # # #         since there are 2 constructor arguments, any instantition of this class 
# # # # # #         will require 2 variables
# # # # # #         '''

# # # # # #         self.var_x = x  # var_x is an instance variable
# # # # # #         self.var_y = y  # var_x is another instance variable

# # # # # #     def display_x(self):  # this is a method so at least the self arguments is required
# # # # # #         print(self.var_x) # to display the current instance varaible self has to be used

# # # # # #     def display_y(self, z):  # this is a method so at least the self arguments is required
# # # # # #         print(z)
# # # # # #         print(self.var_y) # to display the current instance varaible self has to be used
# # # # # #         print(self.var_y * z)

# # # # # #     def distanceFromOrigin(self):
# # # # # #         self.sum = self.var_x**2 + self.var_y**2
# # # # # #         return self.sum

# # # # # # point1 = Point(12,34)
# # # # # # point2 = Point(23,45)

# # # # # # print(  point1.var_x )
# # # # # # print(  point1.distanceFromOrigin()  )


# # # # # # class City():
# # # # # #     '''class to represent and manipulate citi variables '''

# # # # # #     def __init__ (self, x, y, z):
# # # # # #         self.name = x
# # # # # #         self.population = y
# # # # # #         self.province = z

# # # # # # cityName = ['Toronto', ' Calgary', 'Hamilton', 'Ottawa']
# # # # # # population = [234567, 800909, 80808080, 8080080]
# # # # # # province = ['ON', 'AB', 'ON', 'ON']

# # # # # # city_tuple = zip(cityName, population, province)

# # # # # # list_of_city_instances = [City(x,y,z) for x,y, z in city_tuple ]

# # # # # # print(list_of_city_instances)


# # # # # # we can pass class instances as arguments

# # # # # # class Point():
# # # # # #     ''' class to represent and manipulate x,y coordinates of a point '''
# # # # # #     # constrctor method or initializor
# # # # # #     def __init__ (self, x, y):
# # # # # #         self.x = x 
# # # # # #         self.y = y 

# # # # # #     # __str__ makes the display of the object pretty, it gets returned when print(instance) is executed
# # # # # #     def __str__ (self):
# # # # # #         return 'Point at ({}, {}) .. {}'.format(self.x, self.y, 'gibberesh')

# # # # # #     # defining the distance function as a method
# # # # # #     def half_of_points(self, instance2):
# # # # # #         new_x = (self.x + instance2.x)/2
# # # # # #         new_y = (self.y + instance2.y)/2
# # # # # #         return Point(new_x, new_y)
 
# # # # # #     def __add__ (self, instance2):
# # # # # #         return Point(self.x + instance2.x, self.y + instance2.y)

# # # # # # # instantiating
# # # # # # point1 = Point(12,23)
# # # # # # point2 = Point(78,34)

# # # # # # point3 = point1 + point2
# # # # # # print(point3)

# # # # # # point4 = point1.half_of_points(point2)

# # # # # # print(point4)  

# # # # # # print(point4.x)
# # # # # # print(point4.y)

# # # # # # help(filter)

# # # # # class Fruit():
# # # # #     def __init__ (self, name, price, quantity):
# # # # #         self.name = name
# # # # #         self.price = price
# # # # #         self.quantity = quantity

# # # # #     def __str__ (self):
# # # # #         return '{} is priced as {} and has a quanity of {} in stock'.format(self.name, self.price, self.quantity)

# # # # # fruit_names = ['Apples', 'Pears', 'Bananas', 'Grapes']        
# # # # # fruit_prices = [12,45,1,3]
# # # # # fruit_qty = [100,34,789,12]

# # # # # fruit_tuples = zip(fruit_names, fruit_prices, fruit_qty)

# # # # # fruit_instance_list = [Fruit(n,p,q) for n,p,q in fruit_tuples ]

# # # # # sorted_fruits_on_name = sorted(fruit_instance_list, key = lambda self: self.name, reverse=True)
# # # # # sorted_fruits_on_price = sorted(fruit_instance_list, key = lambda self: self.price)
# # # # # sorted_fruits_on_qty = sorted(fruit_instance_list, key = lambda self: self.quantity)

# # # # # print('\n*** REVERSE sorting instances based on names ***')
# # # # # print( [instance.name  for instance in sorted_fruits_on_name ] )
# # # # # print( [ (instance.name, instance.price, instance.quantity)  for instance in sorted_fruits_on_name ] )

# # # # # print('\n*** sorting instances based on prices ***')
# # # # # print( [instance.price  for instance in sorted_fruits_on_price ] )
# # # # # print( [ (instance.name, instance.price, instance.quantity)  for instance in sorted_fruits_on_price ] ) 

# # # # # print('\n*** sorting instances based on Quantity ***')
# # # # # print( [instance.quantity  for instance in sorted_fruits_on_qty ] )
# # # # # print( [ (instance.name, instance.price, instance.quantity)  for instance in sorted_fruits_on_qty ] ) 


# # # # # GOAL: to create a Class that has 3 instance variables, the values are 
# # # # # stored in 3 different lists, each of length 5, the values are positional
# # # # # create 5 instances of the class and sort the instances according to the 
# # # # # price

# # # # list1 = ['apples', 'oranges', 'peaches', 'carrots', 'papaya']
# # # # list2 = [100, 200, 13, 2, 120]
# # # # list3 = [12.5, 22.3, 25.8, 2.3, 45.56]

# # # # class Class1(): # defining the class
# # # #     '''this class represents and manipulates fruits  
# # # #     '''
# # # #     def __init__ (self, fruit, quantity, price): # constructor
# # # #         self.fruit = fruit
# # # #         self.quantity = quantity
# # # #         self.price = price

# # # #     def __str__ (self): # special function to display instance as a string rather than pointing to its address when printed
# # # #         return '{} has Quantity {} and price {}'.format(self.name, self.quantity, self.price)

# # # # # instantiating 

# # # # instance_list = [ Class1(x,y,z) for x,y,z in zip(list1, list2, list3) ]

# # # # print('*** Sorted list according to names ***')
# # # # print('*** this will print the address of the sorted instances ***')
# # # # print(sorted(instance_list, key=lambda self: self.fruit))

# # # # print('*** this is printing the values as tuples of the sorted list ***')
# # # # print( [ (instance1.fruit, instance1.quantity, instance1.price) for f in sorted(instance_list, key=lambda self: self.fruit)     ] )

# # # # import random

# # # # class Pet():

# # # #     boredom_decrement = 4
# # # #     hunger_decrement = 6
# # # #     hunger_thereshold = 10
# # # #     boredom_thereshold = 5
# # # #     sounds = ['mrrp']

# # # #     def __init__(self, name = 'Kitty'):  
# # # #         self.name = name
# # # #         self.hunger = random.randrange(self.hunger_thereshold)
# # # #         self.boredom = random.randrange(self.boredom_thereshold)
# # # #         self.sounds = self.sounds.copy() # making a copy so the changes to one instnace does not change others

# # # #     def __str__(self):
# # # #         self.state = self.mood()
# # # #         return 'I am {} and I am feeling {}'.format(self.name, self.state)

# # # #     def clock_tick(self):
# # # #         self.hunger += 1
# # # #         self.boredom += 1

# # # #     def mood(self):
# # # #         if self.hunger > self.hunger_thereshold:
# # # #             return 'hungry'

# # # #         if self.boredom > self.boredom_thereshold:
# # # #             return 'bored'
# # # #         else:
# # # #             return 'happy'

# # # #     def teach(self, learn1):
# # # #         self.taught_word = learn1
# # # #         (self.sounds).append(self.taught_word )
# # # #         self.reduce_boredom()

# # # #     def hi(self):
# # # #         print(  random.choice(self.sounds)  ) #  self.sounds[random.randrange ( len(self.sounds) )]
# # # #         self.reduce_boredom()

# # # #     def reduce_boredom (self):
# # # #         self.boredom -= self.boredom_decrement
# # # #         if self.boredom < 0:
# # # #             self.boredom = 0

# # # #     def feed(self):
# # # #         self.hunger -= self.hunger_decrement
# # # #         if self.hunger < 0:
# # # #             self.hunger = 0


# # # # p1 = Pet("Fido")
# # # # print(p1)
# # # # for i in range(10):
# # # #     p1.clock_tick()
# # # #     print(p1)
# # # # p1.feed()
# # # # p1.hi()
# # # # p1.teach("Boo")
# # # # for i in range(10):
# # # #     p1.hi()
# # # # print(p1)


# # # #inherentace - a child inheriting from parent

# # # class Person():
# # #     def __init__(self, name, yob, weight):
# # #         self.name = name
# # #         self.yob = yob
# # #         self.weight = weight

# # #     def __str__(self):
# # #         return '{}: {} {}kgs'.format(self.name, self.yob, self.weight)

# # #     def get_yob(self):
# # #         return self.yob


# # # class Student(Person):
# # #     def __init__(self, name, yob, weight, grade):
# # #         Person.__init__(self, name, yob, weight)
# # #         self.grade = grade

# # #     def __str__(self):
# # #         return '{}: {} {}kgs Grade {}'.format(self.name, self.yob, self.weight, self.grade)

# # #     def parent_class_str(self):
# # #         return Person.__str__(self)

# # # # Govind = Person('Govind', 1981, 75)
# # # # print(Govind)

# # # Person1 = Person('Govind', 1981, 75)
# # # print(Person1)

# # # Student1 = Student ('Deepak', 1986, 80, 'Bachelors')
# # # print(Student1)
# # # print(Student1.parent_class_str())


# # from random import randrange

# # # Here's the original Pet class
# # class Pet():
# #     boredom_decrement = 4
# #     hunger_decrement = 6
# #     boredom_threshold = 5
# #     hunger_threshold = 10
# #     sounds = ['Mrrp']
# #     def __init__(self, name = "Kitty"):
# #         self.name = name
# #         self.hunger = randrange(self.hunger_threshold)
# #         self.boredom = randrange(self.boredom_threshold)
# #         self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class

# #     def clock_tick(self):
# #         self.boredom += 1
# #         self.hunger += 1

# #     def mood(self):
# #         if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
# #             return "happy"
# #         elif self.hunger > self.hunger_threshold:
# #             return "hungry"
# #         else:
# #             return "bored"

# #     def __str__(self):
# #         state = "     I'm " + self.name + ". "
# #         state += " I feel " + self.mood() + ". "
# #         # state += "Hunger %d Boredom %d Words %s" % (self.hunger, self.boredom, self.sounds)
# #         return state

# #     def hi(self):
# #         print(self.sounds[randrange(len(self.sounds))])
# #         self.reduce_boredom()

# #     def teach(self, word):
# #         self.sounds.append(word)
# #         self.reduce_boredom()

# #     def feed(self):
# #         self.reduce_hunger()

# #     def reduce_hunger(self):
# #         self.hunger = max(0, self.hunger - self.hunger_decrement)

# #     def reduce_boredom(self):
# #         self.boredom = max(0, self.boredom - self.boredom_decrement)


# # class Dog(Pet):
# #     sounds = ['Woof', 'Ruff']

# #     def feed(self):
# #         super().feed()
# #         print("Arf! Thanks!")

# # d1 = Dog("Astro")
# # d1.feed()

# # class Bird(Pet):
# #     sounds = ["chirp"]
# #     # name = 'prisca'
# #     def __init__(self, name="jason", chirp_number=2):
# #         super().__init__() # call the parent class's constructor
# #         # basically, call the SUPER -- the parent version -- of the constructor, with all the parameters that it needs.
# #         self.name = name
# #         self.chirp_number = chirp_number # now, also assign the new instance variable

# #     def hi(self):
# #         for i in range(self.chirp_number):
# #             print(self.sounds[randrange(len(self.sounds))])
# #         self.reduce_boredom()

# # b1 = Bird('pristina')
# # # b1.teach("Polly wanna cracker")
# # b1.hi()
# # print(b1)
# # print(b1.sounds)
# # print(b1.name)
# # print(b1.hunger)

# # class Pokemon():
# #     attack = 12
# #     defense = 10
# #     health = 15
# #     p_type = "Normal"

# #     def __init__(self, name, level = 5):
# #         self.name = name
# #         self.level = level

# #     def train(self):
# #         self.update()
# #         '''
# #         def update(self):
# #             self.health_boost = 5
# #             self.attack_boost = 3
# #             self.defense_boost = 2
# #             self.evolve = 10
# #         '''
# #         self.attack_up()
# #         self.defense_up()
# #         self.health_up()
# #         self.level = self.level + 1
# #         if self.level%self.evolve == 0:
# #             return self.level, "Evolved!"
# #         else:
# #             return self.level

# #     def attack_up(self):
# #         self.attack = self.attack + self.attack_boost
# #         return self.attack

# #     def defense_up(self):
# #         self.defense = self.defense + self.defense_boost
# #         return self.defense

# #     def health_up(self):
# #         self.health = self.health + self.health_boost
# #         return self.health

# #     def update(self):
# #         self.health_boost = 5
# #         self.attack_boost = 3
# #         self.defense_boost = 2
# #         self.evolve = 10

# #     def __str__(self):
# #         self.update()
# #         return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

# # class Grass_Pokemon(Pokemon):
# #     attack = 15
# #     defense = 14
# #     health = 12

# #     def update(self):
# #         self.health_boost = 6
# #         self.attack_boost = 2
# #         self.defense_boost = 3
# #         self.evolve = 12

# #     def moves(self):
# #         self.p_moves = ["razor leaf", "synthesis", "petal dance"]

# #     def action(self):
# #         return '{} knows a lot of different moves!'.format(self.name)

# #     def train(self):
# #         self.update()
# #         self.defense_up()
# #         self.health_up()
# #         self.level = self.level + 1
# #         if self.level >= 10:
# #             self.attack_up()
# #         if self.level%self.evolve == 0:
# #             return self.level, "Evolved!"
# #         else:
# #             return self.level     

# # p1 = Grass_Pokemon('Belle')

# # for i in range(10):
# #     print('--------------')
# #     print('level: {}'.format(p1.level))
# #     print('attack: {}'.format(p1.attack))
# #     print(" *** training *** ")
# #     p1.train()

# # p1.attack_up()    



# # import unittest

# # class GovindTestCases (unittest.TestCase):
# #     def test_upper(self):
# #         self.assertEqual('foo'.upper(), 'FOO')

# #     def test_lower(self):
# #         self.assertEqual('foo'.lower(), 'Foo')
  
# # if __name__ == '__main__':
# #     unittest.main()

# # print('print me, I am after the __name__ == "main" ')


# import unittest

# print(dir(unittest.TestCase))
import unittest

class GovindUnitTesting(unittest.TestCase):

    def test_check(self):
        self.assertEqual( [1,2].append(3), [1,2,3] )

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')   

unittest.main()


