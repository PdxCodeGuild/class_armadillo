#my first lab!
'''
from turtle import *

fillcolor('blue')

begin_fill()



edge_length = 0
i = 0
while i < 100:
	forward(edge_length)
	right(144)

	edge_length += 4

done()
'''
from turtle import *

fillcolor('blue')

begin_fill()

from turtle import *

edge_length = 200
n_sides = 20

i = 0
while i < n_sides:
	forward(edge_length/n_sides)
	right(360/n_sides)
	i = i + 1


penup()
setposition(-50, -70)
pendown()
forward(120)
setposition(0,-70)
right(90)
forward(100)
right(30)
forward(80)
penup()
setposition(0,-170)
pendown()
left(60)
forward(80)
penup()
setposition(0,150)
pendown()
forward(100)
right(144)
forward(100)
right(144)
forward(100)
right(144)
forward(100)
right(144)
forward(100)

done()