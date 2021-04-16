from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        paddle_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=paddle_y)

    def move_down(self):
        paddle_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=paddle_y)
