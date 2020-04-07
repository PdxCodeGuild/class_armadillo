# PDX Code Guild Fullstack Course
# Lab 01 Turtle
# Samuel Purdy
# 4/6/2020

from turtle import *

# Moves the Pen to a specific position while also picking it up so to not draw unnecessary lines.
def move_pen(x,y):
    penup()
    setposition(x,y)
    pendown()

# Moves the Pen home while also picking it up so to not draw unnecessary lines.
def move_pen_home():
    penup()
    home()
    pendown()

# Draws grass
def draw_grass():
    fillcolor('green')
    begin_fill()
    forward(1000)
    right(90)
    forward(500)
    right(90)
    forward(1000)
    right(90)
    forward(500)
    right(90)
    end_fill()

# Draws sky
def draw_sky():
    fillcolor(0,150,255)
    begin_fill()
    forward(1000)
    left(90)
    forward(700)
    left(90)
    forward(1000)
    left(90)
    forward(700)
    left(90)
    end_fill()

# Draws sun
def draw_sun():
    i = 0
    fillcolor(255,255,0)
    begin_fill()
    circle(25)
    end_fill()

# Draws the body
def draw_body():
    right(90)
    forward(100)

# Draws the legs
def draw_legs():
    right(15)
    forward(120)
    backward(120)
    left(30)
    forward(120)
    backward(120)

# Draws the head
def draw_head():
    left(90)
    backward(10)
    i = 0
    
    fillcolor(255,255,255)
    begin_fill()
    while i < 8:
        forward(20)
        right(45)
        i += 1
    end_fill()
    forward(10)

# Draws the arms
def draw_arms():
    left(90)
    forward(10)
    left(15)
    forward(90)
    backward(90)
    right(90)
    forward(45)
    right(90)
    forward(45)

# Sets the color mode to add RGB specific colors
colormode(255)

# Moves the pen to an off-screen position to draw the grass.
move_pen(-500, -200)
draw_grass()

# Moves the pen to an off-screen position to draw the sky.
move_pen(-500, -200)
draw_sky()

# Moves the pen to a specific position to draw the sun.
move_pen(300, 300)
draw_sun()

# Sets the pent home to draw the lower body.
move_pen_home()
pendown()
draw_body()
draw_legs()

# Resets position back at the origin
left(165)
forward(100)

# Draws the arms and legs.
draw_head()
draw_arms()

done()