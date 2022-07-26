from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time
from snake import Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Xenzai")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")




is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score += 1
        score.write_score()
    if not score.boundary_check(snake):
        #is_game_on = False
        score.reset()
        snake.reset()

    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            #is_game_on = False
            score.reset()
            snake.reset()



screen.exitonclick()