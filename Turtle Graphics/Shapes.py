from turtle import Turtle, Screen
from random import choice
import turtle

donatelllo = Turtle()
donatelllo.shape("turtle")

colors = ['medium blue', 'green yellow', 'orange', 'red', 'black', 'green',"CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        donatelllo.forward(100)
        donatelllo.right(angle)


for sides in range(3, 11):
    donatelllo.color(choice(colors))
    draw_shape(sides)

screen = Screen()
screen.exitonclick()