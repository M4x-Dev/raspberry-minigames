from src.sense_matrix import SenseMatrix
from src.pong.wall import Wall
from sense_hat import SenseHat
from time import sleep

white = [0, 0, 190]
black = [0, 0, 0]

sense = SenseHat()
game_matrix = SenseMatrix()

player_wall = Wall(4, 0, white)
computer_wall = Wall(4, 7, white)

while True:
    for event in sense.stick.get_events():
        if "up" in event.direction and "pressed" in event.action:
            player_wall.move(-1)
        elif "down" in event.direction and "pressed" in event.action:
            player_wall.move(1)

    game_matrix.fill_pixels(black)
    player_wall.draw(game_matrix)
    computer_wall.draw(game_matrix)
    game_matrix.draw(sense)
