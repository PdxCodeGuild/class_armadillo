"""
Lab 1: Turtle

Explanation

Turtle is a python module that allows us to move a virtual turtle around the screen using programming 
statements. This turtle has a position and a heading. Below are a list of commands, you can more in the 
turtle docs.

-forward(distance) moves the turtle forward the given number of pixels
-left(angle) and right(angle) turns the turtle left or right by the given angle (in degrees)
-color(color_name) sets the pen's color, which can be penup() penup() penup()
-penup() raises the pen, a line won't be drawn when the turtle moves, pendown() lowers the pen again
-setposition(x, y) moves the turtle to the given position
-fillcolor(color_name) sets the fill color, begin_fill() indicates you'd like to begin filling in whatever 
 you draw, end_fill() actually fills the shape in.

Use these functions to draw a stick figure with a head, body, two arms, and two legs. Once you're done, 
go through the examples below and create your own drawing.
"""

from turtle import *

#preferences
hideturtle()
bgcolor(("black")) #background color
color('white') 
fillcolor('white')
pensize(5)

penup() 
setposition(0, 60) # so the image is centered
pendown()

#head
begin_fill()
circle(40)
end_fill()

penup()
goto(0, 50) #start/end location for torso
right(90)
pendown()

#Left shoulder
begin_fill()
right(90)
forward(60)
left(90)

#left arm
forward(140)
left(90)
forward(22.5) #left hand
left(90)
forward(115)
right(90) 
forward(10) #left armpit
right(90)

#legs
forward(260) #chest down to foot
left(90)
forward(25)
left(90)
forward(160) #left leg
right(90)
forward(10) #groin
right(90)
forward(160)
left(90)
forward(25)
left(90)
forward(260) #right foot to chest

#right arm
right(90)
forward(10) #right armpit
right(90)
forward(115)
left(90)
forward(22.5) #right hand
left(90)
forward(140)
left(90)
goto(0, 50) #torso start location
end_fill()
done()
