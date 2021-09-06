from turtle import Turtle, Screen
import turtle as t
import  random
# timmy = Turtle()
# for i in range (0,4):
#     timmy.forward(100)
#     timmy.right(90)
t.colormode(255)
arrow = Turtle()

# for i in range(15):
#     arrow.forward(10)
#     arrow.penup()
#     arrow.forward(10)
#     arrow.pendown()
corlor_list=["orange red", "indigo", "magenta", "deep sky blue"]
# def draw_shape (side_number):
#     d_degree =360/side_number
#     for _ in range(side_number):
#         arrow.forward(100)
#         arrow.right(d_degree)
# for choice in range (3,8):
#     arrow.color(random.choice(corlor_list))
#     draw_shape(choice)
def random_corlor():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    ran_corlor = (r,b,g)
    return ran_corlor
# d_degree =[0,90,180,270]
#
# for _ in range(100):
#     arrow.pencolor(random_corlor())
#     arrow.forward(30)
#     a = random.choice(d_degree)
#     arrow.setheading(a)
def set_circle(choice):
    global arrow
    for _ in range(int(360/choice)):
        arrow.circle(100)
        arrow.color(random_corlor())
        arrow.setheading(arrow.heading()+choice)

set_circle(5)


screen = Screen()
screen.exitonclick()

