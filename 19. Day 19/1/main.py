from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()


def move_forward():
    tom.forward(10)


def move_backward():
    tom.backward(10)


def turn_left():
    new_heading = tom.heading() - 10
    tom.setheading(new_heading)


def turn_right():
    new_heading = tom.heading() + 10
    tom.setheading(new_heading)


def s_clear():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=s_clear, key="x")
screen.exitonclick()
