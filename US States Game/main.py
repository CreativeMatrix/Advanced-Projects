import pandas
from turtle import Screen, Turtle
from tkinter import messagebox


states = pandas.read_csv('50_states.csv')
screen = Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
screen.bgpic('blank_states_img.gif')

guessed_states = []

while len(guessed_states) < 50:
    state_answer = screen.textinput(title=f"{len(guessed_states)}/50 States Guessed Correctly", prompt="Type the name of a State and click OK or type 'Exit' to end game.").title()
    list_of_states = states.state.to_list()

    if state_answer == 'Exit':
        missing_states = []
        for state in list_of_states:
            if state not in guessed_states:
                missing_states.append(state)
        messagebox.showinfo(title="GAME OVER", message=f"You've missed a few states: {missing_states}")
        break

    elif state_answer in list_of_states:
        turtle = Turtle()
        turtle.hideturtle()
        turtle.penup()
        choosen_state = states[states.state == state_answer] 
        turtle.goto(x=float(choosen_state.x), y=float(choosen_state.y))
        turtle.write(choosen_state.state.item(), align='left', font=('Arial', 8, 'normal'))
        guessed_states.append(state_answer)

if len(guessed_states) == 50:
    messagebox.showinfo(title="YOU WIN!", message="CONGRATULATIONS! YOU HAVE GUESSED ALL 50 STATES!")

