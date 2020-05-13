#Lab 1: Turtle

from turtle import *

#head line 6 

i = 0
pensize(width=10)
pencolor('red')
while i < 100:
    forward(5)
    left(110/30)
    i = i + 1

right(2)
pendown()

pensize(width=30)
pencolor('blue')
# right arm
forward(230)# this mean going forward 230 pixel 
backward(230)
#left arm
backward(230)
#center
forward(230)
pensize(width=40)
pencolor('yellow')
# body
penup()
right(90)# rotate 90 degree right 
#allow to start drawing 
pendown()
forward(150)
#to go center

pensize(width=30)
pencolor('yellow')
#right leg
right(45)
forward(50)
right(180)
penup()
forward(50)
right(90)
pendown()
#left leg
forward(50)
right(180)# rotate 180 degree right 
penup()
forward(50)
right(45)
pendown()


done()

