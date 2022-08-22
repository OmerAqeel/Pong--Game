from turtle import Turtle, Screen
from paddle import Paddle
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
game_Screen.listen()

# Paddle1 controls
game_Screen.onkey(key="Up", fun=paddle1.moveUp)
game_Screen.onkey(key="Down", fun=paddle1.moveDown)

# Paddle2 controls
game_Screen.onkey(key="w", fun= paddle2.moveUp)
game_Screen.onkey(key="s", fun=paddle2.moveDown)

in_the_Game = True

while in_the_Game:
    game_Screen.update()

















game_Screen.exitonclick()
