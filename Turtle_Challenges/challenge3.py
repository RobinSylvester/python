from turtle import Turtle, Screen
colors = ['red','blue','green','yellow','pink','black','purple','violet','maroon','brown']
tim = Turtle()
i = 0

for _ in range(3, 11):
    for j in range(_):
        tim.forward(100)
        tim.left(360//_)
    tim.pencolor(colors[i])
    i += 1





screen = Screen()
screen.exitonclick()