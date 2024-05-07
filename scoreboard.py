from turtle import Turtle
# Change scoreboard variables here: (self.write______)
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

# use turtle.write and turtle.clear


class Scoreboard(Turtle):

    def __init__(self):
        """Adds attributes to the scoreboard class"""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align = "center",font=("Courier", 40, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 40, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
