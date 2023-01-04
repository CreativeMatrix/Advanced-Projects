from turtle import Turtle   

X_AXIS = 0
Y_AXIS = [-450, -400, -350, -300, -250, -200, -150, -100, -50 , 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
Y = [-425, -375, -325, -275, -225, -175, -125, -75, -25, 25, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525]


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor('white')
        self.speed('fastest')
        self.hideturtle()
        self.width(10)
        self.penup()
        self.goto(0, -465)
        self.create_net()
        self.create_border()


    def create_net(self):
        for turtle in range(0, 20):
            self.pendown()
            self.goto(X_AXIS, Y_AXIS[turtle])
            self.penup()
            self.goto(X_AXIS, Y[turtle])

        
    def create_border(self):
        self.width(3)
        self.penup()
        self.goto(x=765, y=-470)
        self.pendown()
        self.goto(x=765, y=510)
        self.goto(x=-770, y=510)
        self.goto(x=-770, y=-470)
        self.goto(x=765, y=-470)