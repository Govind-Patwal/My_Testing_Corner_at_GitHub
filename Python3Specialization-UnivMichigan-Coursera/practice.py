''' a turtle program that draws on the screen askign 
the user to inpur the background color or the screen, 
set the name of the turtle, set the color and the penwidth '''

import turtle

user_bgcolor = input('Please enter the screen color: ')


window = turtle.Screen()
window.bgcolor(user_bgcolor)

# dia = input('Enter the name of your turtle: ')
dia = turtle.Turtle()

dia_color = input('Enter the color of the line: ')
dia_width = int(input('Enter the width of the line: '))

dia.color(dia_color)
dia.pensize(dia_width)

dia.forward(200)
dia.left(90)

dia.forward(200)
dia.left(90)

dia.forward(200)
dia.left(90)

dia.forward(200)
dia.left(90)

window.exitonclick()



