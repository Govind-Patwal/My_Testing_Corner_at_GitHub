# total_secs = int(input("Please enter the number of seconds you wish to convert"))


# hours = total_secs // 3600
# secs_still_remaining = total_secs % 3600
# minutes =  secs_still_remaining // 60
# secs_finally_remaining = secs_still_remaining  % 60

# print("Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining)

import turtle
window = turtle.Screen()
window.bgcolor('Blue')          # set the screen color as Blue

dia = turtle.Turtle()       # create an instance of the class Turtle and name it dia
dia.color('white')          # color dia white
dia.pensize(4)            # set the width to 4

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

window.exitonclick()