from turtle import Screen, time
from snake import Snake
from food import Food
from score import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_start = True
while game_start:
    screen.update()
    time.sleep(0.1)
    snake.move()
     
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_segments()
        score.score_refresh()
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        game_start = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_start = False
            score.game_over()
        

        

    

screen.exitonclick()
