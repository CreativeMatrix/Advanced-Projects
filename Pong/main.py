from turtle import Screen
from paddles import Paddle
from net import Net
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.title('Pong')
screen.screensize(canvwidth=1280, canvheight=720)
screen.bgcolor('black')
screen.tracer(0)


ball = Ball()
net = Net()

l_paddle = Paddle((-755, 0))
r_paddle = Paddle((750, 0))

l_player_score = Scoreboard((-100, 400))
r_player_score = Scoreboard((100, 400))
    

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

play_game = True
while play_game:
    screen.update()
    ball.move()

    if r_paddle.ycor() > 450:
        r_paddle.stop_go_up()
    elif r_paddle.ycor() < -415:
        r_paddle.stop_go_down()
    if l_paddle.ycor() > 450:
        l_paddle.stop_go_up()
    elif l_paddle.ycor() < -415:
        l_paddle.stop_go_down()

    if ball.ycor() > 500 or ball.ycor() < -460:
        ball.wall_bounce_y()
        
    if ball.distance(r_paddle) < 50 and ball.xcor() > 730 or ball.distance(l_paddle) < 50 and ball.xcor() < -735:
        ball.wall_bounce_x()
        
        
    if ball.xcor() > 760:
        ball.reset_position()
        l_player_score.keep_score()

    if ball.xcor() < -765:
        ball.reset_position()
        r_player_score.keep_score()


screen.exitonclick()
