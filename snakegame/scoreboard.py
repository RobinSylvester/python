from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.high_score = 0
        with open("data.txt") as f:
            self.high_score = int(f.read())
        self.pencolor("white")
        self.penup()
        self.sety(270)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score : {self.score}  High Score : {self.high_score}", align="center",
                   font=("courier", 20, "bold"))

    def boundary_check(self, snake):
        if snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.xcor() < -290 or snake.head.ycor() > 290:
            self.reset()
            return 0
        return 1

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.write_score()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align="center", font=("calibri", 30, "bold"))