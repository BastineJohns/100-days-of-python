from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, paddle_coordinates):
        super().__init__()
        self.coordinates = paddle_coordinates
        self.shape("square")
        self.color("white")
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(paddle_coordinates)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)   

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y) 

    def reset_position(self):
        self.goto(self.coordinates)    
