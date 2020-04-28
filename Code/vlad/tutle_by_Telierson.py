# tutle by Telierson: 

import turtle
import random
def create_tree(branch_len):
    angle = random.randint(20, 30)
    shrink = random.uniform(0.6, 0.8)
    if branch_len > 10:
        turtle.forward(branch_len)
        turtle.left(angle)
        create_tree(branch_len*shrink)
        turtle.right(angle*2)
        create_tree(branch_len*shrink)
        turtle.left(angle)
        turtle.backward(branch_len)
turtles = []
number_of_turtles = random.randint(5, 10)
for number in range(0, number_of_turtles):
    turtles.append([number])
x = -400
turtle.speed(100)
turtle.left(90)
turtle.color('brown')
for t in turtles:
    turtle.up()
    x += random.randint(75, 125)
    turtle.goto(x, random.randint(-200, 100))
    turtle.down()
    create_tree(random.randint(75, 120))
turtle.done()