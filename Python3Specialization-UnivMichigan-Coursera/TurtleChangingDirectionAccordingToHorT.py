#### START - cool program to get a turtle move according to a coin flip  #### 

import turtle

def turtle_in_screen(x,y):
    '''
    Function to check if the turtle is still in the screen
    >>> turtle_in_screen(500,500)
    False
    '''
    right_bound = window.window_width()/2
    left_bound = -(window.window_width()/2)
    upper_bound = window.window_height()/2
    lower_bound = -(window.window_height()/2)   
    if (x > right_bound or x < left_bound) or (y > upper_bound or y < lower_bound):
        return False
    else:
        return True

def turtle_movement():
    '''
    Funciton to move and stop the turtle
    >>> turtle_movement()
    Enter Head or Tail (enter "stop" to end): 
    >>> head
    '''
    while True:
        head_or_tail = input('Enter Head or Tail (enter "stop" to end): ')
        if head_or_tail in ['stop', 'Stop']:
            break
        elif head_or_tail not in ['Head','head', 'Tail', 'tail']:
            print('Invalid input...')  
            continue  
        elif head_or_tail in ['Head','head']:
            alex.left(90)    
            alex.forward(50)
        elif head_or_tail in ['Tail','tail']:
            alex.right(90)    
            alex.forward(50)
        alex_x_coord = alex.xcor()
        alex_y_coord = alex.ycor()
        continue_moving = turtle_in_screen(alex_x_coord,alex_y_coord)
        if continue_moving == False:
            break

window = turtle.Screen()   
window.bgcolor('green')

alex = turtle.Turtle()
alex.shape('turtle')

turtle_movement()

window.exitonclick()

#### END - cool program to get a turtle move according to a coin flip  #### 


    

