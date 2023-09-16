import turtle as t

MOVE_DISTANCE = 20
POSITION = [(0,0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        # creating snake
        self.snakeBody = []
        for pos in POSITION:
            self.add_part(pos)
        
        self.snake_head = self.snakeBody[0]

    
    def add_part(self, position):
        turtle = t.Turtle(shape="square")
        turtle.penup()
        turtle.goto(position)
        turtle.color("white")
        self.snakeBody.append(turtle)
    
    def extend(self):
        self.add_part(self.snakeBody[-1].position())

    def move(self):
        for i in range(len(self.snakeBody) - 1, 0, -1):
            newX = self.snakeBody[i - 1].xcor()
            newY = self.snakeBody[i - 1].ycor()
            self.snakeBody[i].goto(newX, newY)
        self.snake_head.fd(MOVE_DISTANCE)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
        

