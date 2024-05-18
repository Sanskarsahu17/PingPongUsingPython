from turtle import Turtle,Screen
from scoreBoard import ScoreBoard

import ball
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
gameIsOn = True
# Creating  a screen of 600X400
screen.setup(width=600,height=400)
screen.tracer(0)
screen.listen()
p1=Paddle()
p2=Paddle()
p1.setToLeft()
p2.setToRight()
b = Ball()
sb = ScoreBoard()
while(gameIsOn):
    time.sleep(0.1)
    screen.update()

    b.startMove()
    screen.onkey(key="w", fun=p1.moveUp)
    screen.onkey(key="s", fun=p1.moveDown)
    screen.onkey(key="8", fun=p2.moveUp)
    screen.onkey(key="5", fun=p2.moveDown)
    # Rebound logic
    if(b.ycor() > 180 or b.ycor() < -180 ):
        b.bounceBack()
    # If ball hits the end wall
    if(b.xcor() > 290 or b.xcor() < -290):
        gameIsOn = False
    # peddle hitting ball logic
    if (p2.distance(b) <40 and b.xcor()>250 or p1.distance(b)<40 and  b.xcor()<-250):
        b.hit()
    if (b.xcor()>280):
        sb.updatePlayer1Score()
        b.resetBall()
    if (b.xcor()<-280):
        sb.updatePlayer2Score()
        b.resetBall()



screen.exitonclick()