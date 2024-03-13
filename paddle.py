from turtle import Turtle, Screen
screen = Screen()
screen.tracer(0)

class Paddle(Turtle):
    
    def __init__(self, pos):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.turtlesize(5, 1)
        self.penup()
        self.y_pos = 0
        self.pos = pos
        self.goto(self.pos, self.y_pos)
        self.speed(0)

    def up(self):
        self.y_pos = self.y_pos + 40
        self.goto(self.pos, self.y_pos)
        
    def down(self):
        self.y_pos = self.y_pos - 40
        self.goto(self.pos, self.y_pos)
        
    def reset_paddle(self, pos):
        self.goto(pos, 0)