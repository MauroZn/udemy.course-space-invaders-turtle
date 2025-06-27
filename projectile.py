from turtle import Turtle

MOVE_DISTANCE = 40

class Projectile(Turtle):

    def __init__(self):
        super().__init__("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=0.1, stretch_len=0.5)
        self.goto(1000,1000)

    def spawn(self,x,y):
        self.goto(x, y)

    def move(self, move_speed):
        self.forward(move_speed)
