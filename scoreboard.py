from turtle import Turtle

class Scoreboard:
    def __init__(self, w_screen):
        self.writer = Turtle(visible=False)
        self.writer.color('black')
        self.writer.penup()
        self.screen = w_screen
        self.score = 0
        with open(file='highscore.txt') as f:
            self.high_score = int(f.read())
        self.screendimensions = (self.screen.window_width(), self.screen.window_height())

    def drawscore(self):
        self.writer.clear()
        self.writer.goto(0, self.screendimensions[1]/2-28)
        self.writer.write(arg=f"Score: {self.score} | High score: {self.high_score}", align='center', font=('Arial', 18, 'bold'))

    # def gameover(self):
    #     self.writer.goto(0,0)
    #     self.writer.write(arg='Game Over', align='center', font=('Arial', 30, 'bold'))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file='highscore.txt', mode='w') as f:
                f.write(f"{self.score}")

        self.score = 0
        self.drawscore()

