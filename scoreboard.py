from turtle import Turtle
from snake import Snake
timmy = Snake
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.write(f"Score : {self.score}", align = "center", font=("courier", 20, "normal"))
        self.hideturtle()

    def update_score(self):
        self.write(f"Score : {self.score}", align="center", font=("courier", 20, "normal"))


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",align="center", font=("courier", 20, "normal") )


    def inc_score(self):
        self.score +=1
        self.clear()
        self.update_score()







