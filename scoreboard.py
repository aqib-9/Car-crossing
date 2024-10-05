from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-300,250)
        self.write(f"Level:{self.level}", align="left", font=FONT)
    def win(self):
        self.level+=1
    def update_score(self):
        self.clear()
        self.win()
        self.write(f"Level:{self.level}", align="left", font=FONT)

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(-30,0)
        self.write(f"Game Over!!", align="left", font=FONT)
