from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 500)
user_choice = screen.textinput(title="Let choice your Turtle!", prompt="Enter a color (red, green, blue, black or yellow)")
color_turtle = ["red", "green", "blue", "black", "yellow"]
position_t = ["-60", "-30", "0", "30", "60"]
all_turtle = []

for count_t in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color_turtle[count_t])
    new_turtle.goto(x=-230, y=float(position_t[count_t]))
    all_turtle.append(new_turtle)
if user_choice:
    is_race_on = True
while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_on = False
            turtle_win = turtle.pencolor()
            if user_choice == turtle_win:
                print (f"You win ! The turtle {turtle_win} fastest!")
            else:
                print(f"You lose ! The turtle {turtle_win} fastest!")

        ran_distance = random.randint(0,10)
        turtle.forward(ran_distance)










screen.exitonclick()

