from turtle import Screen
from Snake import Snake
import time
import Food
from scoreboard import Scorecard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food.Food()
scorecard = Scorecard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.random_food()
        snake.extend()
        scorecard.increase_score()

    # Detect collision with wall

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -290:
        scorecard.reset_game()
        snake.reset()

    # Detect collision with tail

    for n in snake.segments[1:]:
        if snake.head.distance(n) < 10:
            scorecard.reset_game()
            snake.reset()

