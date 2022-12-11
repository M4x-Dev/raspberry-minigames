from src.sense_matrix import SenseMatrix
from src.flappy_bird.tube_set import TubeSet
from src.flappy_bird.bird import Bird
from sense_hat import SenseHat
from random import randint
from time import sleep

bird_color = [0, 0, 190]
tube_color = [0, 190, 0]
black = [0, 0, 0]
red = [255, 0, 0]

sense = SenseHat()
game_matrix = SenseMatrix()

bird = Bird(1, 4, bird_color)
tubes = []
tubes.append(TubeSet(3, 6, tube_color))

while True:
    # Reduce the game speed
    sleep(0.1)

    # Detect joystick events
    for event in sense.stick.get_events():
        if "pressed" in event.action:
            bird.jump()

    # Move all tubes
    for tube in tubes:
        tube.move(-1)

    # Draw the game
    game_matrix.fill_pixels(black)
    bird.draw(game_matrix)
    for tube in tubes:
        tube.draw(game_matrix)
    game_matrix.draw(sense)
