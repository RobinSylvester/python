import colorgram
import turtle
from turtle import Turtle, Screen
from random import randint, choice

# rgb_colors = []
# colors = colorgram.extract('hirst.jpg', 25)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
# print(rgb_colors)

tim = Turtle()
tim.hideturtle()
turtle.colormode(255)
tim.penup()
tim.goto(-200, -200)

colors = [(222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (126, 40, 61), (21, 86, 61), (59, 48, 37), (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190), (57, 71, 39), (197, 102, 134), (156, 191, 185), (30, 67, 58),  (166, 204, 202), (62, 26, 45), (145, 165, 181), (6, 79, 111)]

for i in range(0, 10):
    for j in range(0, 10):
        tim.dot(15, choice(colors))
        tim.penup()
        tim.forward(50)
    tim.setx(-200)
    tim.sety(tim.ycor()+50)


screen = Screen()
screen.exitonclick()