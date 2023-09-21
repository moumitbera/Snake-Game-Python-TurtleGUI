ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


import turtle


class scoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 280)
        self.color("white")
        self.score = 0
        self.high_score = self.get_high_score()
        self.ht()
        self.update_score()
        

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.get_high_score()}", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        if self.score > self.high_score:
            self.set_high_score(self.score)

        self.score = 0
        self.update_score()

    #write the highscore
    def set_high_score(self, score):
        with open(file="high_score.txt", mode="w") as file:
            file.write(str(score)) #str() converts into string, we could have also used f string
    
    #returns the highest score as an integer
    def get_high_score(self):
        with open(file="high_score.txt") as file:
            highScore = file.read()
        return int(highScore)
