from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()
        self.speed('fastest')

    def refresh(self):
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        self.goto(x, y)
