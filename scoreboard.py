from turtle import Turtle

UPDATE_FONT = ("Courier", 18, "normal")
OVER_FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-250, 250)
        self.update_level = f"Level: {self.level}"
        self.write(self.update_level, align = "left", font = UPDATE_FONT)

    def game_over(self):
        self.goto(0 ,0)
        self.write("Game Over!", align = "center", font = OVER_FONT)


