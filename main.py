from turtle import Turtle, Screen
import time
import random
from paddle import *
from ball import Ball
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')
scoreboard = Score()

game_on = True
while game_on:
    scoreboard
    screen.update()
    screen.listen()
    screen.onkey(r_paddle.up, 'Up')
    screen.onkey(r_paddle.down, 'Down')
    screen.onkey(l_paddle.up, 'w')
    screen.onkey(l_paddle.down, 's')
    ball.move()
    if ball.distance(r_paddle) < 50.0 and ball.xcor() > 340 or ball.distance(l_paddle) < 50.0 and ball.xcor() < -340:
        ball.bounce()
    if ball.xcor() > 400:
        l_paddle.reset() 
        r_paddle.reset()
        r_paddle = Paddle(350)
        l_paddle = Paddle(-350)
        scoreboard.l_scored()
        scoreboard.update_scoreboard()
        ball.reset_ball()
        ball.move()
    elif ball.xcor() < -400:
        l_paddle.reset() 
        r_paddle.reset()
        r_paddle = Paddle(350)
        l_paddle = Paddle(-350)
        scoreboard.r_scored()
        scoreboard.update_scoreboard()
        ball.reset_ball()
        ball.move()
    game_on = scoreboard.game_over()

screen.exitonclick()