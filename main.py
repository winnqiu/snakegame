from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
game_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if food.distance(snake.head) < 15:
        food.refresh()
        scoreboard.update()
        snake.add_seg()

    if snake.collide_wall() or snake.collide_self():
        game_on=False
        scoreboard.game_over()

screen.exitonclick()
