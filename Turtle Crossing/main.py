import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

turtle = Player()
cars = CarManager()
score = Scoreboard()

screen.onkeypress(turtle.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()
    for car in cars.all_cars:
        if car.distance(turtle) < 25:
            score.game_over()
            game_is_on = False

    if turtle.ycor() == 300:
        turtle.start_postition()
        cars.increase_speed()
        score.clear()
        score.increase_level()

screen.exitonclick()