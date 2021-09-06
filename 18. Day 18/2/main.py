import turtle
from turtle import Turtle, Screen
turtle.colormode(255)


dot_draw = Turtle()

dot_draw.speed(100)
dot_draw.setheading(270)
dot_draw.penup()
dot_draw.forward(200)
dot_draw.right(90)
dot_draw.forward(200)
dot_draw.right(180)
dot_draw.dot(10)

dot_draw.ht()

for count_dot in range(1,101):
    dot_draw.dot(20,"red")
    dot_draw.forward(40)

    if count_dot % 10 ==0:
        dot_draw.left(90)
        dot_draw.forward(40)
        dot_draw.left(90)
        dot_draw.forward(400)
        dot_draw.right(180)


















screen = Screen()
screen.exitonclick()
