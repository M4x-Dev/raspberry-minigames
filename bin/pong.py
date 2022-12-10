from src.sense_matrix import SenseMatrix
from src.pong.wall import Wall
from sense_hat import SenseHat

white = [255, 255, 255]
black = [0, 0, 0]

sense = SenseHat()
game_matrix = SenseMatrix()
game_matrix.fill_pixels(black)

player_wall = Wall(4, 0, white)
player_wall.draw(game_matrix)

computer_wall = Wall(4, 7, white)
computer_wall.draw(game_matrix)

game_matrix.draw(sense)
