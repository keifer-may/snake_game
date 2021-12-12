from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        self.score = 0
        super().__init__()
        self.penup()
        self.color("green")
        self.setpos(0,275)
        self.ht()
        self.write(arg=(f"Score: {self.score}"), move= False, align ="center", font=("arial", 16, "normal"))


    def add_point(self):
        self.score += 1
        self.reset()
        self.penup()
        self.color("green")
        self.setpos(0, 275)
        self.ht()
        self.write(arg=(f"Score: {self.score}"), move= False, align ="center", font=("arial", 16, "normal"))


    def game_over(self):
        self.goto(0, 0)
        self.write(arg=(f"GAME OVER"), move= False, align ="center", font=("arial", 16, "normal"))
