from turtle import Turtle, Screen

flash = Turtle()
flash.shape('turtle')
flash.color("yellow")
for _ in range(10):
    flash.forward(10)
    if _ % 2 == 0:
        flash.penup()
    else:
        flash.pendown()

screen = Screen()
screen.exitonclick()
