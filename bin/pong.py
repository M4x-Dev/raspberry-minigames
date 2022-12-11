from src.sense_matrix import SenseMatrix
from src.pong.wall import Wall
from sense_hat import SenseHat
from time import sleep

game_color = [0, 0, 190]
black = [0, 0, 0]

sense = SenseHat()
game_matrix = SenseMatrix()

ball = [4, 4]
ball_velocity = [-1, 1]

player_wall = Wall(4, 0, game_color)
computer_wall = Wall(4, 7, game_color)

while True:
    sleep(0.25)
    for event in sense.stick.get_events():
        if "up" in event.direction and "pressed" in event.action:
            player_wall.move(-1)
        elif "down" in event.direction and "pressed" in event.action:
            player_wall.move(1)

    for i in range(len(ball)):
        ball[i] += ball_velocity[i]

    game_matrix.fill_pixels(black)
    game_matrix.set_pixel(ball[0], ball[1], game_color)
    player_wall.draw(game_matrix)
    computer_wall.draw(game_matrix)
    game_matrix.draw(sense)
