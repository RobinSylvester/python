FONT = ("Courier", 24, "normal")

from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.pencolor("black")
        self.penup()
        self.goto(-200, 255)

    def write_score(self):
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Score : {self.score}\nGame Over", align="center", font=FONT)

