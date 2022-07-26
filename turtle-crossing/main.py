import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
cars = CarManager()
score = Scoreboard()
score.write_score()
screen.listen()
screen.onkey(turtle.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    for car in cars.all_cars:
        if car.xcor() < -280:
            cars.all_cars.remove(car)
            car.hideturtle()
           # print(len(cars.all_cars))
        if car.distance(turtle) < 20:
            game_is_on = False
            score.game_over()

    if turtle.is_reached():
        score.score += 1
        score.write_score()
        turtle.to_starting_point()
        cars.level_up()


screen.exitonclick()