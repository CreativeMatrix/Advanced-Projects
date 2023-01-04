from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(x=-280, y=260)
        self.write(f"Level: {self.level}", align='left', font=FONT)
        

    def increase_level(self):
        self.level += 1
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color('red')
        self.write("GAME OVER", align='center', font=('Arial', 15, 'normal'))