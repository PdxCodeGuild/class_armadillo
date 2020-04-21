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

fillcolor('blue')
begin_fill()

#head
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
#torso
right(90)
forward(20)
left(90)
forward(200)
left(90)
forward(140)
left(90)
forward(200)
left(90)
forward(110)
#legs
left(90)
forward(400)
left(90)
forward(80)
left(90)
forward(400)

end_fill()
done()
