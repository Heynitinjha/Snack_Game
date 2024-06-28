from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0,280)
        self.Update_screen()
        self.hideturtle()

    def Update_screen(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over")

    def increase_score(self):
        self.score += 1
        self.clear()
        self.Update_screen()