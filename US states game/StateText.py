from  turtle import Turtle


class StateText(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_state(self, state, x, y):
        self.goto(x, y)
        self.write(state, align="left", font=("calibri", 12, "bold"))
