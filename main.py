from snake import Snake
from turtle import Screen
from time import sleep
from food import Food
from scoreboard import Scoreboard

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
SCREEN_COLOR = 'darkgreen'
FOOD_COLOR = 'red'
SNAKE_COLOR = 'grey'
SCORE_LIMIT = WINDOW_WIDTH/20 * WINDOW_HEIGHT/20

screen = Screen()
screen.bgcolor(SCREEN_COLOR)
screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
screen.tracer(0)
food = Food(size=10, color=FOOD_COLOR, screen=screen)
snake = Snake(screen, food, snake_color=SNAKE_COLOR)
scoreboard = Scoreboard(screen)
food.dropfood()
scoreboard.drawscore()

while True:
    snake.setheadingonkey()
    snake.move()

    if snake.eatfood():
        scoreboard.score += 1
        scoreboard.drawscore()
        snake.addsegment()
        food.clear_food()
        if scoreboard.score == SCORE_LIMIT:
            print('YOU ARE A BEAST!')
            break
        food.dropfood()

    if snake.hitwall() or snake.hit_itself():
        scoreboard.reset_score()
        snake.reset_body()
        screen.update()
        sleep(1)


    screen.update()
    sleep(0.1)
screen.exitonclick()
