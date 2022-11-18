from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')


class ScoreBoard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('White')
        self.penup()
        self.setposition(0, 270)

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', move=False, align=ALIGNMENT, font=FONT)