from turtle import Turtle
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.shape("square")
        self.color("white")
        self.goto(x=350, y=0)

    def moveUp(self):
        if self.ycor() < 240:       # To make sure the paddle does not moves any forward after reaching the maximum boundary of the screen
            Y = self.ycor()
            self.sety(y=Y + 40)

    def moveDown(self):
        if self.ycor() > -240:      # To make sure the paddle does not moves any forward after reaching the maximum boundary of the screen
            Y = self.ycor()
            self.sety(y=Y - 40)

    def move_to_other_side(self):
        self.goto(x=-350, y=0)
