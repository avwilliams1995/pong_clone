from turtle import Turtle, Screen
screen = Screen()
import time

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 200)
        self.write(self.l_score, align= 'center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align= 'center', font=('Courier', 80, 'normal'))
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align= 'center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align= 'center', font=('Courier', 80, 'normal'))

    def r_scored(self):
        self.r_score +=1

    def l_scored(self):
        self.l_score +=1

    def game_over(self):
        if self.l_score == 11 or self.r_score == 11:
            self.goto(0, 0)
            self.write('Game Over!', align= 'center', font=('Courier', 80, 'normal'))
            return False
        else:
            return True