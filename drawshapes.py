
from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = -250
y_pos = -150
t.penup()
t.setposition(x_pos, y_pos)

### Write your code below:
def draw_shapes(x_pos,y_pos):
    for m in range(500):
        for i in range(4):
            t.pendown()
            t.forward(50)
            t.right(90)
        t.penup()
        y_pos = y_pos +50
        x_pos = x_pos +50
        t.setposition(x_pos, y_pos)
    

draw_shapes(x_pos,y_pos)



# Close window on click.
exitonclick()
