from turtle import *

fillcolor('blue')

n_sides = 8
edge_length = 0

i = 0
begin_fill()
while i < 150:
	forward(edge_length)
	right(360/n_sides)
	i = i + 1
	edge_length = edge_length + 1
end_fill()
done()
 