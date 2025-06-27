from turtle import Screen, Turtle
from player_ship import PlayerShip
from ships_manager import ShipsManager
from projectile import Projectile
from scoreboard import Scoreboard
from city import City
import time
import random

screen = Screen()
screen.setup(width=500, height=800)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.tracer(0)

player_ship = PlayerShip()
start_text = Turtle()
ship_manager = ShipsManager()
player_projectile = Projectile()
player_projectile.right(270)
player_projectile.color("red")
scoreboard = Scoreboard()
city = City()

ships_projectiles = []
game_is_on = True
game_started = False
player_is_shooting = False

def start_game():
    global game_started
    game_started = True
    start_text.clear()

def player_shoot():
    global player_is_shooting
    player_projectile.spawn(player_ship.xcor(), player_ship.ycor())
    player_is_shooting = True

def ships_shoot():
    ships_projectile = Projectile()
    ships_projectile.right(90)
    x = ship_manager.all_ships[random.randint(1,len(ship_manager.all_ships)-1)].xcor()
    y = ship_manager.all_ships[random.randint(1,len(ship_manager.all_ships)-1)].ycor()
    ships_projectile.spawn(x, y)
    ships_projectiles.append(ships_projectile)

start_text.hideturtle()
start_text.color("white")
start_text.penup()
start_text.goto(0, 0)
start_text.write("Press DOWN to start the game.",align= "center", font=("Arial", 18, "bold"))

screen.listen()
screen.onkey(start_game, "Down")
screen.onkey(player_ship.left, "Left")
screen.onkey(player_ship.right, "Right")
screen.onkey(player_shoot, "Up")

last_shot_time = 0

while game_is_on:
    screen.update()
    time.sleep(0.05)
    if game_started:
        ship_manager.move_ships()
        current_time = time.time()
        if current_time - last_shot_time >= 1:
            ships_shoot()
            last_shot_time = current_time

    for ship_projectile in ships_projectiles:
        ship_projectile.move(20)

    if player_is_shooting:
        player_projectile.move(30)
    if ships_projectiles:
        for ships_projectile in ships_projectiles:
            if ships_projectile.distance(player_ship) < 10:
                scoreboard.lives -= 1
                scoreboard.update_scoreboard()
                ships_projectile.goto(3000,3000)
                ships_projectiles.remove(ships_projectile)
    if ship_manager.all_ships:
        for ship in ship_manager.all_ships:
            if player_projectile.distance(ship) < 35:
                player_is_shooting = False
                player_projectile.goto(1000,1000)
                ship.goto(2000, 2000)
                ship.update_position()
                ship_manager.all_ships.remove(ship)
                scoreboard.increase_score()
                scoreboard.update_scoreboard()
                break
    else:
        scoreboard.winner()
        game_is_on = False

    if city.parts:
        parts_to_remove = []
        ships_proj_to_remove = []

        # Check ships projectiles against city parts
        for part in city.parts:
            for ships_proj in ships_projectiles:
                if ships_proj.distance(part) < 10:  # increased threshold for reliability
                    parts_to_remove.append(part)
                    ships_proj_to_remove.append(ships_proj)
            # Check player projectile against city parts
            if player_projectile.distance(part) < 20:
                parts_to_remove.append(part)
                player_is_shooting = False
                player_projectile.goto(1000, 1000)

        # Remove marked parts and projectiles
        for part in parts_to_remove:
            part.goto(1000, 1000)
            if part in city.parts:
                city.parts.remove(part)
        for ships_proj in ships_proj_to_remove:
            ships_proj.goto(3000, 3000)
            if ships_proj in ships_projectiles:
                ships_projectiles.remove(ships_proj)
    else:
        scoreboard.game_over()
        game_is_on = False

    if scoreboard.lives == 0:
        scoreboard.game_over()
        game_is_on = False
screen.exitonclick()
