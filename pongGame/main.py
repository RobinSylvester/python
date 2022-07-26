from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Scoreboard()
is_game_on = True

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

while is_game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()
    # wall collision
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()

    # paddle collision
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Ball missing right side
    if ball.xcor() > 400:
        score.update_l_score()
        ball.reset_ball()

    # Ball missing left side
    if ball.xcor() < -400:
        score.update_r_score()
        ball.reset_ball()


screen.exitonclick()