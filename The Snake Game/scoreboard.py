from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.setposition(x=0, y=275)
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 15, "normal" ))
          
        
    def keep_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 15, "normal" ))

    def gameover(self):
        self.goto(0, 0)
        self.color('red')
        self.write('GAME OVER', align='center', font=("Arial", 15, "normal" ))