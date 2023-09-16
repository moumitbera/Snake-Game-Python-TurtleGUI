import turtle as t
import random


class Food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("light steel blue")
        self.speed("fastest")
        self.get_new_food()

    def get_new_food(self):
        randomX = random.choice(range(-280, 280, 20))
        randomY = random.choice(range(-280, 280, 20))
        self.goto(randomX, randomY)
