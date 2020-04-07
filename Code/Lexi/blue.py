# fun with turtle, a Python module
# draw 100 circles of many colors 
# http://docs.python.org/3.1/library/turtle.html 
# http://static.michael0x2a.com/turtle_examples.html 
# http://www.eg.bucknell.edu/~hyde/Python3/TurtleDirections.html

import random
import time
import turtle
t = turtle.Pen()

win = turtle.Screen()
win.bgcolor("lightgreen")
win.title("Love Turtles")

def mycircle(red, green, blue):
	t.color(red, green, blue)
	t.begin_fill()
	x = random.randint(10,100)
	t.circle(x) # draw a circle of random radius
	t.end_fill()
	t.up() # pick up pen
	y = random.randint(0,360)
	t.seth(y) # set heading to random direction
	# t.xcor() is turtle's x; t.ycor() is turtle's y
	if t.xcor() < -300 or t.xcor() > 300:
		t.goto(0, 0) # this is the center 
	elif t.ycor() < -300 or t.ycor() > 300:
		t.goto(0, 0) # this is the center 
	z = random.randint(0,100)
	t.forward(z) # move a random number of pixels
	t.down() # pen down

for i in range(0, 100):
	a = random.randint(0,100)/100.0
	b = random.randint(0,100)/100.0
	c = random.randint(0,100)/100.0
	mycircle(a, b, c) # feed a random color to the function

time.sleep(10)