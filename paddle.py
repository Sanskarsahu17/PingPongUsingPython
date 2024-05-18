from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.penup()
        self.shapesize(0.5,2.5,1)
    def setToLeft(self):
        self.setheading(90)
        self.goto(-270,0)
    def setToRight(self):
        self.setheading(90)
        self.goto(270,0)
    def moveUp(self):
        self.forward(20)
    def moveDown(self):
        self.backward(20)
