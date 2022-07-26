from turtle import Turtle, Screen


def forward():
    tim.forward(10)


def backward():
    tim.back(10)


def left():
    tim.left(2)


def right():
    tim.right(2)


def clear_slate():
    tim.reset()


tim = Turtle()
screen = Screen()
screen.listen()
screen.onkey(key='w', fun=forward)
screen.onkey(key='s', fun=backward)
screen.onkey(key='a', fun=left)
screen.onkey(key='d', fun=right)
screen.onkey(key='c', fun=clear_slate)
screen.exitonclick()
