from turtle import Turtle, Screen
from random import sample, choice,randint

is_race_on = False
def set_color_and_position(turtles_list):
    index = sample(range(0, len(colors)), len(colors))
    i = 0
    x = -230
    y = -150
    for turtle in turtles_list:
        turtle.penup()
        turtle.color(colors[index[i]])
        i += 1
        turtle.goto(x=x, y=y)
        y += 70


colors = ['red', 'blue', 'green', 'yellow', 'pink']
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput('Turtle Race bet', 'Which color turtle would win ?')
tim = Turtle(shape='turtle')
mike = Turtle(shape='turtle')
ron = Turtle(shape='turtle')
leo = Turtle(shape='turtle')
tom = Turtle(shape='turtle')

turtles = [tim, mike, tom, ron, leo]
if user_bet:
    set_color_and_position(turtles)
    is_race_on = True
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 235:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You Win. The {winning_color} turtle is the winner")
            else:
                print(f"You lose. The {winning_color} is the winner.")

        turtle.forward(randint(0, 10))


screen.exitonclick()