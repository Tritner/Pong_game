from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.shape("circle")
        self.penup()
        self.xmove = 1
        self.ymove = 1
        self.speed_move = 0.01

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x,new_y)

    def bounce(self):
        self.ymove *= -1

    def paddle_bounce(self):
        self.xmove *= -1

    def speed_up(self):
        self.speed_move *= 0.7
