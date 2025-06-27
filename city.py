from turtle import Turtle

class City(Turtle):

    def __init__(self):
        super().__init__()
        self.parts = []
        self.offsets = []

        y_values = [-150, -145, -140, -135, -130, -125, -120, -115, -110, -105]

        first_building_layout = []
        x_values = list(range(-200, -140, 5))
        for y in y_values:
            for x in x_values:
                first_building_layout.append((x, y))

        second_building_layout = []
        x_values = list(range(-95, -25, 5))
        for y in y_values:
            for x in x_values:
                second_building_layout.append((x, y))

        third_building_layout = []
        x_values = list(range(25, 95, 5))
        for y in y_values:
            for x in x_values:
                third_building_layout.append((x, y))

        fourth_building_layout = []
        x_values = list(range(140, 200, 5))
        for y in y_values:
            for x in x_values:
                fourth_building_layout.append((x, y))

        layout = first_building_layout + second_building_layout + third_building_layout + fourth_building_layout

        for x, y in layout:
            block = Turtle("square")
            block.penup()
            block.color("red")
            block.shapesize(stretch_wid=0.2, stretch_len=0.2)
            self.parts.append(block)
            self.offsets.append((x, y))

        self.update_position()

    def update_position(self):
        x = self.xcor()
        y = self.ycor()
        for part, (dx, dy) in zip(self.parts, self.offsets):
            part.goto(x + dx, y + dy)

