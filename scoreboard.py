from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('PythonOOP_projects.py/Snake-Game/data.txt') as file:
            self.highscore = int(file.read())
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.write(f'Score: {self.score}  High Score: {
                   self.highscore}', False, "center", ('Arial', 16, 'normal'))
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(f'Score: {self.score}  High Score: {
                   self.highscore}', False, "center", ('Arial', 16, 'normal'))

    def add_score(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.highscore:
            with open('data.txt', 'w') as file:
                self.highscore = self.score
                file.write(str(self.score))
        self.score = 0
        self.update()
