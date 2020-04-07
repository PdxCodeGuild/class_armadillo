# # https://github.com/PdxCodeGuild/class_whatever/blob/master/1%20Python/labs/lab01-turtle.md
# from turtle import *

# forward(200)
# left(75)
# forward(300)


# #circle

# i=0
# while i < 100: # while i is less than 100 steps
#     forward(2) # move forward two paces
#     left(360/100) # rotate 360 degrees over a series of 100 steps
#     i = i +1 # each time adding +1 to the counter
#     # this loop will exit after i reaches 100 steps and draws 360 degrees




# # from turtle import *

# # fillcolor('blue')

# # n_sides = 8
# # edge_length = 0

# # i = 0
# # begin_fill()
# # while i < 150:
# # 	forward(edge_length)
# # 	right(360/n_sides)
# # 	i = i + 1
# # 	edge_length = edge_length + 1
# # end_fill()
# # done()



# penup()


# # from turtle import *

# i = 0
# while i < 4:
#     forward(100)
#     left(90)
#     i = i + 1

# done()

# i=0
# while i < 100:
#     forward(2)
#     left(360/100)
#     i = i +1
from turtle import *

edge_length = 0 # initial start
i = 0
while i < 10: # will stop after 100 of these
	forward(edge_length) #presumably the line preceding
	right(144) # just like radians clockwise

	edge_length += 4

done()