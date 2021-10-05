from turtle import Turtle
from snake import Snake

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        with open("data.txt") as data:
           self.high_score= int(data.read())
        self.goto(0, 270)
        self.write(f"Score : {self.score}", align = "center", font=("courier", 20, "normal"))
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score}  High Score:{self.high_score}", align="center", font=("courier", 20, "normal"))


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER",align="center", font=("courier", 20, "normal") )
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()


    def inc_score(self):
        self.score +=1
        self.update_score()







