from turtle import Turtle

FONT=("Arial", 20, 'normal')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.write(f'Score:{self.score}', align="center", font=FONT)
        self.hideturtle()



    def update(self):
        self.score += 1
        self.clear()
        self.write(f'Score:{self.score}', align="center", font=FONT)

    def game_over(self):
        over=Turtle()
        over.color('white')
        over.write('Game Over',align='center',font=FONT)