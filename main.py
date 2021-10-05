from turtle import Turtle, Screen
import time
from food import Food
from snake import Snake
from scoreboard import Score
speed = ('slow','fast', 'faster','fastest')
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboardtt = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_on = True
i =0
while game_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()


    #Detect collision with food

    if snake.head.distance(food) < 15:
       food.refresh()
       snake.extent_snake(speed[0])
       scoreboardtt.inc_score()

       if int(scoreboardtt.score)>10:
           i+=1
           snake.extent_snake(speed[i])
       elif int(scoreboardtt.score) >20:
           i+=1
           snake.extent_snake(speed[i])
    elif int(scoreboardtt.score)>30:
        i+=1
        snake.extent_snake(speed[i])


    #detect collision with wall
    if snake.head.xcor()>285 or snake.head.xcor()<-285 or snake.head.ycor()<-285  or snake.head.ycor()>285:
        scoreboardtt.reset()
        snake.reset_snake()

    #detect collision with tail
    for seg in snake.snake[1:]:
        if snake.head.distance(seg) < 10:
            scoreboardtt.reset()




screen.exitonclick()