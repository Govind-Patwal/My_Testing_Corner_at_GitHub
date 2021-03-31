'''
Course 3 - Week 3
Functions
'''

# # a very simple function w/o parameters and return value
# def hello():
#     '''
#     This funtion has no paramaters and no return value. 
#     Upon invocation, it prints 'Hello World'
#     >>> hello()
#     Hello World
#     '''
#     print('Hello World')
# hello()         # invoking the function  
# help(hello)     # displaying the docstring of a function




# # funtion to draw a sqare using turtle
# def draw_square(turtle_name, side1):
#     '''
#     This function draws a sqaure, it takes 2 arguments - name of turtle and 
#     length of a side of a square, and gets the turtle to draw it
#     >>> draw_square(50)
#     '''
#     for i in range(4):
#         turtle_name.forward(side1)
#         turtle_name.left(90)
# import turtle
# window = turtle.Screen()
# window.bgcolor('green')
# alex = turtle.Turtle()
# draw_square(alex, 50)
# window.exitonclick()
