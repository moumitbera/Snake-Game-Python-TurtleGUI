import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import scoreBoard


screen = t.Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = scoreBoard()
screen.listen()


# key bindings
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

# moving our snake
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # detect collision w/food
    if snake.snake_head.distance(food) < 22:  # got food
        food.get_new_food()
        snake.extend()
        score_board.increase_score()

    # detect collision w/wall
    if (
        snake.snake_head.xcor() > 290
        or snake.snake_head.xcor() < -290
        or snake.snake_head.ycor() > 290
        or snake.snake_head.ycor() < -290
    ):
        game_on = False
        score_board.game_over()

    # detect collision w/tail or body
    for part in snake.snakeBody[1:]:  # sliced list
        if snake.snake_head.distance(part) < 10:
            game_on = False
            score_board.game_over()


screen.exitonclick()
