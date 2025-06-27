from turtle import Turtle

STARTING_POSITION = (0, -250)
MOVE_DISTANCE = 20

class PlayerShip(Turtle):

    def __init__(self):
        super().__init__("square")
        self.penup()
        self.color("green")
        self.shapesize(stretch_wid=0.75, stretch_len=2)
        self.goto(STARTING_POSITION)

        self.top = Turtle("square")
        self.top.penup()
        self.top.color("green")
        self.top.shapesize(stretch_wid=0.5, stretch_len=0.25)
        self.update_top_position()

        self.middle = Turtle("square")
        self.middle.penup()
        self.middle.color("green")
        self.middle.shapesize(stretch_wid=0.5, stretch_len=1)
        self.update_middle_position()

    def update_top_position(self):
        x = self.xcor()
        y = self.ycor() + 12
        self.top.goto(x, y)

    def update_middle_position(self):
        x = self.xcor()
        y = self.ycor() + 7
        self.middle.goto(x, y)

    def right(self):
        if self.xcor() < 200:
            self.forward(MOVE_DISTANCE)
            self.update_top_position()
            self.update_middle_position()

    def left(self):
        if self.xcor() > -220:
            self.backward(MOVE_DISTANCE)
            self.update_top_position()
            self.update_middle_position()

