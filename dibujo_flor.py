from turtle import *

bgcolor("black")

penup()
goto(-250,130)
pendown()
speed(2)
color("red")
width(4)
begin_fill()
left(50)
forward(110)
circle(35, 200)
right(140)
circle(35, 200)
forward(110)
end_fill()
lt(40)

#Tallo
pensize(5)
speed(5)
color("green")
penup()
goto(0,8)
pendown()
rt(90)
for i in range (210):
    forward(1)
    if i % 10 == 0:
        stamp()

#Flor
penup()
goto(0,22)
pendown()
pensize(2)
speed(20)
hideturtle()
for i in range (80):
    pencolor("red")
    lt(180)
    backward(i*0.1)
    circle(i*0.3,120)
    rt(14)
    forward(i*0.1)
    circle(i*0.3,120)
done()
