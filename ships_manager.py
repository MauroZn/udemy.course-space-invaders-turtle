from turtle import Turtle
from ship import Ship

SHIPS_POSITIONS = [(-180, 140), (-120, 140), (-60, 140), (0, 140), (60, 140), (120, 140), (180, 140),
                   (-180, 170), (-120, 170), (-60, 170), (0, 170), (60, 170), (120, 170), (180, 170),
                   (-180, 200), (-120, 200), (-60, 200), (0, 200), (60, 200), (120, 200), (180, 200),
                   (-180, 230), (-120, 230), (-60, 230), (0, 230), (60, 230), (120, 230), (180, 230),
                   (-180, 260), (-120, 260), (-60, 260), (0, 260), (60, 260), (120, 260), (180, 260)]

class ShipsManager:

    def __init__(self):
        self.all_ships = []
        self.create_ships()
        self.direction = "right"
        self.count = 0

    def create_ships(self):
        for ship_position in SHIPS_POSITIONS:
            new_ship = Ship()
            new_ship.goto(ship_position)
            new_ship.update_position()
            self.all_ships.append(new_ship)

    def move_ships(self):
        if self.direction == "right" and self._reached_right_edge():
            self.direction = "left"
            self.count += 1
        elif self.direction == "left" and self._reached_left_edge():
            self.direction = "right"
            self.count += 1

        if self.count == 2:
            self.direction = "down"
            self.count = 0
        elif self.count == 0:
            self.direction = "right"

        for ship in self.all_ships:
            ship.move(self.direction)

    def _reached_right_edge(self):
        return any(ship.xcor() + 15 >= 230 for ship in self.all_ships)

    def _reached_left_edge(self):
        return any(ship.xcor() - 15 <= -230 for ship in self.all_ships)
