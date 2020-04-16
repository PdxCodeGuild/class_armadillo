# this lab uses turtle to draw a stick man

# must start by importing turtle:
from turtle import *
#draws a circle
circle(75)
#from bottom of circle draws straight line to create neck
right(90)
forward(50)
#turns right 45 degrees and draws arm
right(45)
forward(75)
#goes back over arm, turns left 90 degrees and draws opposite arm
back(75)
left(90)
forward(75)
#goes back over arm, turns right and goes down to create body
back(75)
right(45)
forward(75)
#turns right 45 degrees to create leg
right(45)
forward(75)
#goes back over leg, turns 90 degrees and draws opposite leg.
back(75)
left(90)
forward(75)

done()