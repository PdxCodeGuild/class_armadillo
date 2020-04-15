
# imports functions from turtle.
from turtle import *

# sets the parameter to begin to fill the area black.
fillcolor('black')
begin_fill()

# commands the turtle to start building the stick figure with a circle head.
circle(25)

# sets the parameter to end the fill of the head area of the stick figure.
end_fill()

# commands the turtle to start on the body of the stick figure.
right (90)
forward (50)
left (45)
forward (30)
right (180)
forward (30)
left (90)
forward (30)
left (180)
forward (30)
left (45)
forward (25)
right (90)
forward (30)
left (45)
forward (15)
right (180)
forward (15)
right (45)
forward (60)
right (45)
forward (15)

# commands the turtle to stop when the stick figure is completed.
done ()

