from turtle import Turtle, Screen
from random import randint, choice


leonardo = Turtle()
leonardo.speed(10)
leonardo.width(15)

screen = Screen()
screen.colormode(255)

def move_forward():
    leonardo.forward(25)

def move_backward():
    leonardo.backward(25)

def turn_right():
    leonardo.right(90)
    leonardo.forward(25)

def turn_left():
    leonardo.left(90)
    leonardo.forward(25)

func = [turn_right, turn_left, move_forward, move_backward]

for turtle in range(0, 2000):
    r=(randint(0, 255))
    g=(randint(0, 255))
    b=(randint(0, 255))
    
    leonardo.pencolor(r, g, b)
    choice(func)()


screen.exitonclick()
