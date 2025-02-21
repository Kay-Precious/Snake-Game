from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Screen set-up
screen = Screen()

screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake game")

# Module class call
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Screen listening to keyboard keys set-up
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Switch on/off
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    # detect collision with wall
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    # detect collision with wall --- uncomment if wanted
    # if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
    #     scoreboard.reset()

    # detect collision with tail/body
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) <= 10:
            scoreboard.reset()
            snake.reset()

screen.mainloop()
