from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height =680)
screen.title("Ping Pong")
screen.tracer(0)
ball = Ball()
l_paddle = Paddle((-360,0))
r_paddle = Paddle((360,0))
screen.listen()
score = Scoreboard()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w") 
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x() 

    if ball.xcor() > 330:     
        ball.reset_position()
        score.increase_lscore()
        l_paddle.reset_position()
        r_paddle.reset_position()

    if ball.xcor() < -330:
        ball.reset_position()
        score.increase_rscore()    
        l_paddle.reset_position()
        r_paddle.reset_position()

screen.exitonclick()

