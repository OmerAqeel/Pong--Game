from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.display_score()

    def display_score(self):
        self.goto(x=-100, y=200)
        self.write(self.left_score, align="center", font=("Courier", 80, "normal"))
        self.goto(x=100, y=200)
        self.write(self.right_score, align="center", font=("Courier", 80, "normal"))

    def left_score_increase(self):
        self.clear()
        self.left_score += 1
        self.display_score()

    def right_score_increase(self):
        self.clear()
        self.right_score += 1
        self.display_score()
