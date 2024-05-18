from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.x_cor = 10
        self.y_cor = 10

    def startMove(self):
        x = self.xcor() + self.x_cor
        y = self.ycor() + self.y_cor
        self.goto(x, y)

    def bounceBack(self):
        self.y_cor *= -1

    def hit(self):
        self.x_cor *= -1

    def resetBall(self):

        self.goto(0, 0)
        self.startMove()
