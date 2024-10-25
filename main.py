from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

snake = Snake()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, key="Down")
screen.onkey(snake.left, key="Left")
screen.onkey(snake.right, key="Right")
food = Food()
is_game_on = True
scoreboard = Scoreboard()

while is_game_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        is_game_on = False
        scoreboard.game_over()

    #detect collision

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()






screen.exitonclick()