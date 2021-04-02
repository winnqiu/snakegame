from turtle import Turtle

START_X = 0
START_Y = 0
FORWARD_DIS = 20


class Snake:
    def __init__(self):
        self.snake = []
        self.make_snake()
        self.head = self.snake[0]

    def make_snake(self):
        startx = START_X
        starty = START_Y
        for i in range(3):
            seg = Turtle(shape='square')
            seg.color("white")
            seg.penup()
            seg.goto(startx, starty)
            startx -= 20
            self.snake.append(seg)

    def add_seg(self):
        new_seg=Turtle(shape='square')
        new_seg.color("white")
        new_seg.penup()
        p=self.snake[-1].position()
        new_seg.goto(p)
        self.snake.append(new_seg)

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            x = self.snake[i - 1].xcor()
            y = self.snake[i - 1].ycor()
            self.snake[i].goto(x, y)
        self.snake[0].forward(FORWARD_DIS)

    def up(self):
        if self.head.heading() == 270:
            pass
        else:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90:
            pass
        else:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() == 0:
            pass
        else:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() == 180:
            pass
        else:
            self.head.setheading(0)

    def collide_wall(self):
        if self.head.xcor()>280 or self.head.xcor()<-280 or self.head.ycor()>280 or self.head.ycor()<-280:
            return True
        else:
            return False

    def collide_self(self):
        c=False
        for seg in self.snake[1:]:
            if seg.distance(self.head)<=10:
                c=True
        return c
