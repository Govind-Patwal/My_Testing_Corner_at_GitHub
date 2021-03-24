import turtle
wn = turtle.Screen()

elan = turtle.Turtle()

elan.shape('turtle')

distance = 1
for _ in range(360):
    elan.forward(distance)
    elan.right(1)
    # distance = distance + 10

wn.exitonclick()    