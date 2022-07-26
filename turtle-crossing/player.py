STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.left(90)
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)

    def move_forward(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)

    def is_reached(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False

    def to_starting_point(self):
        self.goto(STARTING_POSITION)

