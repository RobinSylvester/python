from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__("square")
        self.penup()
        self.shapesize(6, 1)
        self.goto(position)
        self.color("white")



    def go_up(self):
        if 230 > self.ycor():
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -230:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

