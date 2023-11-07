from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid= 5 , stretch_len= 1)
        self.goto(position)

    def Up(self):
        self.goto(self.xcor(),self.ycor() + 20)

    def Down(self):
        self.goto(self.xcor(),self.ycor() - 20)






