from turtle import Turtle

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self, snake_screen, snake_food, snake_color: str = 'white'):
        self.screen = snake_screen
        self.food = snake_food
        self.snake_body = []
        self.screen_dimensions = [self.screen.window_height(), self.screen.window_width()]
        self.snake_color = snake_color
        self.buildstartingbody()
        self.snake_head = self.snake_body[0]

    def buildstartingbody(self):
        for i in range(3):
            if i == 0:
                trt = Turtle('square')
                trt.color(self.snake_color)
                trt.pu()
                self.snake_body.append(trt)
            else:
                trt = Turtle('square')
                trt.color(self.snake_color)
                trt.penup()
                trt.goto(self.snake_body[i-1].xcor()-20, self.snake_body[i-1].ycor())
                self.snake_body.append(trt)
                
    def move(self):
        body_len = len(self.snake_body)-1
        for i in range(body_len, -1, -1):
            if i != 0:
                prev_x = self.snake_body[i-1].xcor()
                prev_y = self.snake_body[i-1].ycor()
                self.snake_body[i].goto(prev_x, prev_y)
            else:
                self.snake_body[i].fd(20)
    
    def addsegment(self):
        trt = Turtle('square')
        trt.color(self.snake_color)
        trt.pu()
        last_x = self.snake_body[len(self.snake_body)-1].xcor()
        last_y = self.snake_body[len(self.snake_body)-1].ycor()
        trt.goto(last_x, last_y)
        self.snake_body.append(trt)

    def setheadinup(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def setheadingdown(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def setheadingleft(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def setheadingright(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def setheadingonkey(self):
        self.screen.listen()
        self.screen.onkey(fun=self.setheadinup, key='w')
        self.screen.onkey(fun=self.setheadingdown, key='s')
        self.screen.onkey(fun=self.setheadingleft, key='a')
        self.screen.onkey(fun=self.setheadingright, key='d')
    
    def hitwall(self):
        h_x = self.snake_head.xcor()
        h_y = self.snake_head.ycor()
        height_limit = self.screen_dimensions[0]/2
        width_limit = self.screen_dimensions[1]/2
        if h_y > height_limit-10 or h_y < -height_limit+10 or h_x > width_limit-10 or h_x < -width_limit+10:
            return True
        return False
    
    def hit_itself(self):
        for seg in self.snake_body[1:]:
            if self.snake_head.distance(seg) < 10:
                return True
        return False
    
    def eatfood(self):
        head_x = self.snake_head.xcor()
        head_y = self.snake_head.ycor()
        food_x = self.food.xcor
        food_y = self.food.ycor
        if head_x > food_x-15 and head_x < food_x+15:
            if head_y > food_y-15 and head_y < food_y+15:
                return True
        return False

    def reset_body(self):
        for trt in self.snake_body:
            trt.goto(2000, 2000)
        self.snake_body = []
        self.buildstartingbody()
        self.snake_head = self.snake_body[0]
        self.move()
