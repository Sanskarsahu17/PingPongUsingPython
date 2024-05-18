from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__(shape='classic')
        self.Player1Score = 0
        self.Player2Score = 0
        self.penup()
        self.argument = f"Player 1 : {self.Player1Score}, | Player 2 : {self.Player2Score}"
        self.color("black")
        self.goto(0, 170)
        self.writeScore()
        self.hideturtle()



    def updatePlayer1Score(self):
        self.Player1Score += 1
        self.clear()
        self.writeScore()

    def updatePlayer2Score(self):
        self.Player2Score += 1
        self.clear()
        self.writeScore()

    def writeScore(self):
        self.write(arg=f"Player 1 : {self.Player1Score}, | Player 2 : {self.Player2Score}", align="center", font=('Arial', 10, 'normal'))


    def gameOver(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=('Arial', 20, 'normal'))
