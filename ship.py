from turtle import Turtle

MOVE_DISTANCE = 6

class Ship(Turtle):

    def __init__(self):
        super().__init__()
        self.parts = []
        self.offsets = []

        layout = [
            (-9, 12), (9, 12),
            (-6, 9), (6, 9),
            (-9, 6), (-6, 6), (-3, 6), (0, 6), (3, 6), (6, 6), (9, 6),
            (-12, 3), (-9, 3), (-3, 3), (0, 3), (3, 3), (9, 3), (12, 3),
            (-15, 0), (-12, 0), (-9, 0), (-6, 0), (-3, 0), (0, 0), (3, 0), (6, 0), (9, 0), (12, 0), (15, 0),
            (-15, -3), (-9, -3), (-6, -3), (-3, -3), (0, -3), (3, -3), (6, -3), (9, -3), (15, -3),
            (-15, -6), (-9, -6), (9, -6), (15, -6),
            (-6, -9), (-3, -9), (3, -9), (6, -9),
        ]

        for x, y in layout:
            block = Turtle("square")
            block.penup()
            block.color("green")
            block.shapesize(stretch_wid=0.1, stretch_len=0.1)
            self.parts.append(block)
            self.offsets.append((x, y))

        self.update_position()

    def update_position(self):
        x = self.xcor()
        y = self.ycor()
        for part, (dx, dy) in zip(self.parts, self.offsets):
            part.goto(x + dx, y + dy)

    def move(self, direction):
        """Moves the ship in the given direction ('right' or 'left')"""
        if direction == "right":
            self.forward(MOVE_DISTANCE)
        elif direction == "left":
            self.backward(MOVE_DISTANCE)
        elif direction == "down":
            self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
        self.update_position()

