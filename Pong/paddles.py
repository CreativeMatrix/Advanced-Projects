from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed('fastest')
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=7, stretch_len=1)
        self.penup()
        self.goto(position)
        
               
    def go_up(self):
        y_axis = self.ycor() + 20
        self.goto(self.xcor(), y_axis)

    def go_down(self):
        y_axis = self.ycor() - 20
        self.goto(self.xcor(), y_axis)
   
    def stop_go_up(self):
        y_axis = self.ycor() - 20
        self.goto(self.xcor(), y_axis)

    def stop_go_down(self):
        y_axis = self.ycor() + 20
        self.goto(self.xcor(), y_axis)