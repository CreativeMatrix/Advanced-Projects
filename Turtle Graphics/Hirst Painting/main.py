import colorgram
from turtle import Turtle, Screen
from random import choice

colors = colorgram.extract('spot_painting.jpg', 35)

color_list = []
for color in range(4, 35):
    all_colors = colors[color]
    r = all_colors.rgb.r
    g = all_colors.rgb.g
    b = all_colors.rgb.b
    each_color = (r, g, b)
    color_list.append(each_color)


donatello = Turtle()
donatello.speed(5)
donatello.hideturtle()

screen = Screen()
screen.colormode(255)
y_axis = [-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250] 
x = -250    

for turtle in range(0, 10):
    donatello.penup()
    donatello.goto(x, y_axis[turtle])
    for _ in range(0, 10):
        donatello.dot(20, choice(color_list))
        donatello.penup()
        donatello.forward(50)
        
screen.title("Edward's Digital Spot Painting")
screen.exitonclick()
