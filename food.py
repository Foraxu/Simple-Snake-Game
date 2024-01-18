from turtle import Turtle
import random

class Food:
    
    def __init__(self, size, color, screen):
        self.size = size
        self.color = color
        self.food_item = Turtle(shape='circle', visible=False)
        self.food_item.color(self.color)
        self.screen_dimensions = (screen.window_width(), screen.window_height())
        self.xcor = 0
        self.ycor = 0

    def dropfood(self):
        screen_limits = (self.screen_dimensions[0]/2, self.screen_dimensions[1]/2)
        x_positive_limit = screen_limits[0]
        x_negative_limit = -screen_limits[0]
        y_positive_limit = screen_limits[1]
        y_negative_limit = -screen_limits[1]
        x_random = random.randint(x_negative_limit+10, x_positive_limit-10)
        y_random = random.randint(y_negative_limit+10, y_positive_limit-10)
        self.food_item.pu()
        self.food_item.goto(x_random, y_random)
        self.food_item.pd()
        self.food_item.dot(self.size)
        self.xcor = x_random
        self.ycor = y_random

    def clear_food(self):
        self.food_item.clear()
