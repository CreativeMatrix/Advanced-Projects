from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE
        

    def create_car(self):
        random_car = randint(1, 6)
        if random_car == 1:
            self.car = Turtle('square')
            self.car.shapesize(stretch_wid=1, stretch_len=2)
            self.car.penup()
            self.car.color(choice(COLORS))
            random_yaxis = randint(-250, 250)
            self.car.goto(300, random_yaxis)
            self.all_cars.append(self.car)

    
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    
    def increase_speed(self):
        self.car_speed =+ MOVE_INCREMENT