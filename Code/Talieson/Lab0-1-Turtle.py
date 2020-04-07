from turtle import *

#draw head
penup()
goto(0,80)
pendown()
circle(40)

#draw neck
right(90)
forward(30)

#draw arms
right(45)
forward(40)
left(45)
forward(40)

penup()
goto(0,50)
pendown()
left(45)
forward(40)
left(45)
forward(40)

#onto the rest of the body!

penup()
goto(0,50)
pendown()
right(90)
forward(50)

#legs
right(30)
forward(50)
left(30)
forward(50)

penup()
goto(0,50)
pendown()
forward(50)
left(30)
forward(50)
right(30)
forward(50)

#make him a face

penup()
goto(-20,120)

fillcolor('blue')
begin_fill()
pendown()
circle (7)
end_fill()
penup()
goto(15,120)
begin_fill()
pendown()
circle(7)
end_fill()

penup()
goto(20,100)
color('red')
pendown()
goto(0, 95)

#lets give this rad dude a skateboard!
penup()
goto(60,-85)
pendown()
right(80)
forward(40)
right(8)
forward(70)
right(15)
forward(40)

penup()
color('black')
goto(20,-92)
begin_fill()
pendown()
circle(10)
end_fill()
penup()
goto(-30,-94)
begin_fill()
pendown()
circle(10)
end_fill()

done()