from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=260)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.goto(x=0,y=0)
        self.write("GAME OVER", align= ALIGNMENT, font= FONT)


