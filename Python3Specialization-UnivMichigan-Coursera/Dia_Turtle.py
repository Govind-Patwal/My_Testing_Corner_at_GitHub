''' program to create a graphic on screen using python module turtle, 
    the program asks the user to choose the color of the screen, 
    the color of the pen, and the width of the pen
'''    

import turtle                   # import the module/library turtle
user_screen_color = input('Enter the screen color: ') # enter te screen color
turtle_pen_color = input('Enter pen color: ') # enter the color of the pen
turtle_pen_size = int(input('Enter size: ')) # enter the size of the pen

window = turtle.Screen()    # create an instance of the class Screen
window.bgcolor(user_screen_color)  # set the attribute of the instance

dia = turtle.Turtle()       # create an instance of the class Turtle 
dia.color(turtle_pen_color)          # set the user inputted color
dia.pensize(turtle_pen_size)            # set the user inputted size
dia.shape('turtle')

aryan = turtle.Turtle()     # second instance of class Turtle
aryan.color('pink')         # set the color to pink
aryan.pensize(2)            # set the pensize to 2

ayaansh = turtle.Turtle()   # 3rd instance of the class
ayaansh.color('yellow')     # setting the color to yellow
ayaansh.pensize(3)

dia.forward(50)

aryan.left(120)
aryan.forward(50)

ayaansh.right(120)
ayaansh.forward(50)

dia.left(120)
dia.forward(50)
aryan.left(120)
aryan.forward(50)
ayaansh.left(120)
ayaansh.forward(50)

dia.left(120)
dia.forward(50)
aryan.left(120)
aryan.forward(50)
ayaansh.left(120)
ayaansh.forward(50)



dia.up()
dia.forward(150)
dia.down()

distance = 1
for _ in range(360):
    dia.forward(distance)
    dia.right(1)
    # distance = distance + 10


dia.left(100)

dia.up()
dia.forward(150)
dia.down()

distance = 1
for _ in range(360):
    dia.forward(distance)
    dia.right(1)
    # distance = distance + 10


window.exitonclick()