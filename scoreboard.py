ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


import turtle


class scoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 280)
        self.color("white")
        self.score = 0
        self.ht()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER!\nFinal Score: {self.score}", align=ALIGNMENT, font=FONT)
