from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Score (Turtle):
    def __init__ (self):
        super().__init__()
        self.score = 0
        with open ("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,260)      
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}", False,align = ALIGNMENT, font = FONT )       

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}") 
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        self.reset()
        self.home()
        self.write("Game Over", False, align = ALIGNMENT, font = FONT )
