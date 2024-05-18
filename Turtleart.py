import turtle
from turtle import Turtle, Screen
import random

tuktuk = Turtle()
screen = Screen()
tuktuk.shape("turtle")
turtle.colormode(255)
tuktuk.speed(0)
color = ["blue", "green", "red", "cyan", "magenta", "orange", "black", ]


#random color

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


# # draw Shapes
#
# for i in range(3, 11):
#     size = i
#     angle = 360 / size
#     tuktuk.pencolor(random_color())
#     for _ in range(size):
#         tuktuk.forward(100)
#         tuktuk.right(angle)
#
# # Random walk
#
# for _ in range(300):
#     angle = [0, 90, 180, 270]
#     tuktuk.pencolor(random_color())
#     tuktuk.width(5)
#     tuktuk.forward(30)
#     tuktuk.setheading(random.choice(angle))


#Draw a Spirograph

def spirograph(size):
    for _ in range(int(360 / size)):
        tuktuk.color(random_color())
        tuktuk.circle(100)
        tuktuk.setheading(tuktuk.heading() + size)


spirograph(5)

screen.exitonclick()
