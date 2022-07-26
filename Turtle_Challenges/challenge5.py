import turtle
from turtle import Turtle, Screen
from random import randint
colors = ['red','blue','green','yellow','pink','black','purple','violet','maroon','brown']


tim = Turtle()
tim.speed("fastest")
turtle.colormode(255)
size_of_gap = 5


def random_color():
    r = randint(0,255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def draw_circle(r):
    tim.circle(r)
    tim.forward(5)


def tilt_position(size_of_gaps):
    tim.setheading(tim.heading() + size_of_gaps)
    tim.pencolor(random_color())


for i in range(int(360/size_of_gap)):
    draw_circle(100)
    tilt_position(size_of_gap)




screen = Screen()
screen.exitonclick()