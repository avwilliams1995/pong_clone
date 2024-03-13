from turtle import Turtle, Screen
screen = Screen()
screen.tracer(0)
import time

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.turtlesize(1, 1)
        self.penup()
        self.y_pos = 0
        self.setheading(20)
        self.l_score = 0
        self.r_score = 0
        self.speed(0)
        self.spd = 3
        
    def move(self):
        self.fd(self.spd)
        self.check_wall()

    def reset_ball(self):
        time.sleep(2)
        self.goto(0,0)
        self.setheading(180.0 - self.heading())
        self.spd = 3

    def check_wall(self):
        if self.ycor() > 285.0:
            self.setheading(360.0 - self.heading())
        if self.ycor() < -285.0:
            self.setheading(360.0 - self.heading())

    def bounce(self):
        self.spd += .3
        self.setheading(180.0 - self.heading())
            

            


