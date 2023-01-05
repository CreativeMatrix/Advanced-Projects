from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.setposition(x=0, y=275)
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font=("Arial", 15, "normal" ))   
        
    def keep_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font=("Arial", 15, "normal" ))

    def gameover(self):
        self.goto(0, 0)
        self.color('red')
        self.write('GAME OVER', align='center', font=("Arial", 15, "normal" ))

    def keep_highscore(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.score = 0
            self.clear()
            self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font=("Arial", 15, "normal" ))
            with open('data.txt', 'w') as data:
                data.write(str(self.high_score))
