import time
from turtle import Turtle, Screen
from snake import Snake

screen = Screen()
screen.screensize(canvwidth=600, canvheight= 600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My snake game")

snake = Snake

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()











screen.exitonclick()