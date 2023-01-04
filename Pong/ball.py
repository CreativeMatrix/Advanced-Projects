from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('blue')
        self.shape('circle')
        self.penup()
        self.x_location = 2
        self.y_location = 2
    
    def move(self):
        new_x = self.xcor() + self.x_location
        new_y = self.ycor() + self.y_location
        self.goto(new_x, new_y)

    def wall_bounce_y(self):
        self.y_location *= -1

    def wall_bounce_x(self):
        self.x_location *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.wall_bounce_x()

        
        

