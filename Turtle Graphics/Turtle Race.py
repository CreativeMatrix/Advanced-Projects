from turtle import Turtle, Screen
from random import randint, choice
from tkinter import messagebox


screen = Screen()
screen.setup(width=800, height=500)
screen.title("The Teenage Mutant Ninja Turtle Race")

colors = ['blue', 'purple', 'red', 'orange']
y_axis = [-100, -50, 0, 50]
x_axis = -390

turtle_list = []
for turtles in range(0, 4):
    turtle = Turtle(shape='turtle',)
    turtle.penup()
    turtle.color(colors[turtles])
    turtle.goto(x_axis, y_axis[turtles])
    turtle_list.append(turtle)

user_choice = screen.textinput(title='TMNT Race', prompt="Which Turtle do you think will win? Write a color: " )

if user_choice:
    race_on = True

while race_on:
    random_turtle = choice(turtle_list)
    random_turtle.forward(randint(0, 10))
    if random_turtle.xcor() >= 380:
        race_on = False
        if user_choice == random_turtle.pencolor():
            messagebox.showinfo(title='Win Results', message="YOU WIN!")
        else:
            messagebox.showinfo(title='Win Results', message="YOU LOSE!")

screen.exitonclick()
