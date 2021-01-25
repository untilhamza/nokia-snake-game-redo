from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('../../../Desktop/data.txt' , 'r') as data: # dont' have to put C:
            self.high_score = int(data.read())
        # self.file = open('data.txt', mode='r')
        # self.high_score = int(self.file.read())
        # self.file.close()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('/Users/sansh/Desktop/data.txt', 'w') as data:
                data.write(f'{self.high_score}')
            # file = open('data.txt', mode='w')
            # file.write(str(self.high_score))
            # file.close()
            # need to write this new score to the file here
        self.score = 0
        self.update_scoreboard()