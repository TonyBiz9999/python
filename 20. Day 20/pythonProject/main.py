import time
from turtle import Turtle, Screen

screen = Screen()
screen.screensize(canvwidth=600, canvheight= 600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My snake game")
segmens = []
x_position = [0, -20, -40]
for segment in range(0, 3):
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(x_position[segment], 0)
    segmens.append(new_segment)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(2, 0, -1):
        new_x = segmens[seg_num - 1].xcor()
        new_y = segmens[seg_num - 1].ycor()
        segmens[seg_num].goto(new_x, new_y)

    segmens[0].forward(20)










screen.exitonclick()