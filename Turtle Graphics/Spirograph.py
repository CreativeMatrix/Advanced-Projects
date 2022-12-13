from turtle import Turtle, Screen
from random import randint

raphael = Turtle()
raphael.speed(50)

screen = Screen()
screen.colormode(255)


for turtle in range(int(360 / 5)):
    r=(randint(0, 255))
    g=(randint(0, 255))
    b=(randint(0, 255))
    raphael.pencolor(r, g, b)
    raphael.left(5)
    raphael.circle(100)


screen.exitonclick()
