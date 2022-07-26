import turtle
from turtle import Turtle, Screen
from random import randint
colors = ['red','blue','green','yellow','pink','black','purple','violet','maroon','brown']


tim = Turtle()
directions = [tim.left, tim.right]
angles = [0, 90, 180, 270]
tim.pensize(15)
tim.speed(6)
turtle.colormode(255)


def random_color():
    r = randint(0,255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def move_random():
    tim.forward(50)
    rand_angle = angles[randint(0, len(angles)-1)]
    directions[randint(0, 1)](rand_angle)
    tim.pencolor(random_color())


for i in range(100):
    move_random()










screen = Screen()
screen.exitonclick()