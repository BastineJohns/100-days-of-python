from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.update_score()
        

    def update_score(self):
        self.write(f"Score = {self.score}", False, align= ALIGNMENT, font= FONT )

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align= ALIGNMENT, font= FONT )    



        
    def score_refresh(self):
        self.clear()
        self.score += 1 
        self.update_score()   

