import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
tuktuk = Turtle()
screen = Screen()
tuktuk.speed(0)
tuktuk.penup()
tuktuk.hideturtle()

# import colorgram
#
# rgb_color = []
# colors = colorgram.extract("HirstPainting.jpg", 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
#
# print(rgb_color)


color_list = [(208, 158, 96), (234, 213, 101), (41, 104, 144), (149, 78, 57), (130, 168, 194), (202, 137, 162),
              (148, 65, 83), (24, 40, 55), (204, 90, 68), (169, 159, 55), (139, 180, 152), (193, 89, 121),
              (59, 117, 93), (26, 44, 36), (223, 171, 187), (63, 46, 34), (91, 154, 104), (44, 161, 182), (237, 212, 7),
              (226, 175, 167), (13, 96, 75), (41, 59, 99), (179, 189, 213), (99, 125, 168), (65, 33, 43), (104, 43, 59)]


tuktuk.setheading(255)
tuktuk.forward(300)
tuktuk.setheading(0)
number_of_dot = 100

for dot_count in range(1, number_of_dot + 1):

    tuktuk.dot(20, random.choice(color_list))
    tuktuk.forward(50)
    if dot_count % 10 == 0:
        tuktuk.setheading(90)
        tuktuk.forward(50)
        tuktuk.setheading(180)
        tuktuk.forward(500)
        tuktuk.setheading(0)


screen.exitonclick()
