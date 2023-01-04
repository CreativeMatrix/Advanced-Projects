from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(position)
        self.write(self.score, align='center', font=("Courier", 80, 'normal'))
        
    def keep_score(self):
        self.score += 1
        self.clear()
        self.write(self.score, align='center', font=("Courier", 80, 'normal'))
