from turtle import Turtle

X_AXIS = [0, -20, -40]
MOVE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):
        for position in range(3):
            snakes = Turtle()
            snakes.shape('square')
            snakes.color('white')
            snakes.penup()
            snakes.goto(x=X_AXIS[position], y=0)
            self.snake_list.append(snakes)
            
    def increase_tail(self):
        add_snake = Turtle()
        add_snake.shape('square')
        add_snake.penup()
        add_snake.hideturtle()
        add_snake.goto(x=self.snake_list[-1].xcor(), y=self.snake_list[-1].ycor())
        self.snake_list.append(add_snake)
        add_snake.color('white')
        add_snake.showturtle()
        

    def move(self):
        for snake in range(len(self.snake_list) - 1, 0, -1):
            x = self.snake_list[snake - 1].xcor()
            y = self.snake_list[snake - 1].ycor()
            self.snake_list[snake].goto(x, y)
        self.snake_list[0].forward(MOVE_FORWARD)
    
    def up(self):
        if self.head.heading() != DOWN: 
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    

