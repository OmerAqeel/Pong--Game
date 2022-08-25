# Pong-Game
A classic pong game created using Python, its module turtle was used to create the GUI and OOP has been used to fulfil the functional requirements of the game.
## Modules used in the program
1) turtle 
2) time

### turtle
The turtle module provides turtle graphics primitives, in both object-oriented and procedure-oriented ways. Because it uses tkinter for the underlying graphics, it needs a version of Python installed with Tk support.

You can learn more about it in its documentation 👉 https://docs.python.org/3/library/turtle.html#turtle.done

### time 
This module provides various time-related functions. For related functionality, see also the datetime and calendar modules.

You can learn more about it in its documentation 👉  https://docs.python.org/3/library/time.html
## The game is divided into 4 classes
1) main.py
2) paddle.py
3) ball.py
4) scoreboard.py

### main.py
This is main class of the program where all the instances from the all the other classes are created and used to build the game logic. All the conditions that the player might face during the game is tackled in this class i.e hitting the ball, scoring point, ball bouncing back from the edges.

### paddle.py
This is the class created for the paddle instance that is created in the main.py, the class inherits from Turtle class from the turtle module. The class includes methods that allows the player to control the paddle on the screen i.e. moveUP(), moveDown().

### ball.py
This the class created for the ball object that is created in the main.py, this class also inherits from Turtle class from the turtle module. The class includes methods for the ball in the pong game, move() method used to move the ball on the screen, bounce_y() method used to bounce the ball from the wall/edges/boundaries of the screen, bounce_x() method for bouncing the ball when it is hit by the player and resetpos() which positions the ball back to the origin (x=0, y=0) coordinates.


### Graphical User Interface (GUI)
<img width="801" alt="Screenshot 2022-08-24 at 01 59 02" src="https://user-images.githubusercontent.com/93266569/186280630-f76ba35e-e0d5-4eb8-93ce-78ce01eed564.png">

