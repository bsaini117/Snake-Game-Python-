from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
screen.listen()
food = Food()
scoreboard = ScoreBoard()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
scoreboard.update_scoreboard()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    #detect collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    #detect tail collision
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False






screen.exitonclick()