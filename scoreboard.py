from turtle import Turtle

FONT = ("Arial", 18, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 5
        # with open("data.txt") as data:
        #     self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,370)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  |  ", align="right", font=FONT)
        self.write(f"Lives: {self.lives}", align="left", font=FONT)

    # def update_high_score(self):
    #     if self.score > self.high_score:
    #         self.high_score = self.score
    #         with open("data.txt", mode="w") as data:
    #             data.write(f"{self.high_score}")
    #     self.score = 0
    #     self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

    def winner(self):
        self.goto(0, 0)
        self.write("YOU WIN", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()