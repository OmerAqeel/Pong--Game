from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
#Screen
game_Screen = Screen()
game_Screen.setup(width=800,height=600)
game_Screen.bgcolor("black")
game_Screen.title("The Classic Pong")
game_Screen.tracer(0)

# Paddles
paddle1 = Paddle()      # Paddle that will be on the right side of the screen
paddle2 = Paddle()      # Paddle that will be on the left side of the screen
paddle2.move_to_other_side()    # moving the paddle to the left side

# Game Objects
ball = Ball()
game_Screen.listen()
score = ScoreBoard()

# Paddle1 controls
game_Screen.onkey(key="Up", fun=paddle1.moveUp)
game_Screen.onkey(key="Down", fun=paddle1.moveDown)

# Paddle2 controls
game_Screen.onkey(key="w", fun= paddle2.moveUp)
game_Screen.onkey(key="s", fun=paddle2.moveDown)

in_the_Game = True

while in_the_Game:
    time.sleep(0.05)   # This will allow the ball to move on a regular pace
    game_Screen.update()
    ball.move()
# Detecting the collision between the wall and the ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
# Detecting the collision between the paddle and ball
    if (ball.distance(paddle1) < 40 and ball.xcor()> 320) or (ball.distance(paddle2) < 40 and ball.xcor()< -320):
        ball.bounce_x()
#Detecting if the paddle misses the ball and its a goal
    if ball.xcor() == -400:                 # When the right paddle scores a point
        score.right_score_increase()        # Point given to the right paddle
        ball.resetpos()                     # Ball set back to the origin position 
        
    if ball.xcor() == 400:                  # When the left paddle scores a point
        score.left_score_increase()
        ball.resetpos()




game_Screen.exitonclick()
