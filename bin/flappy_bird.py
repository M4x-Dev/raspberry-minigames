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
tubes = [TubeSet(randint(0, 5), 8, tube_color)]

second_iteration = True
while True:
    # Reduce the game speed
    sleep(0.15)

    # Detect joystick events
    for event in sense.stick.get_events():
        if "pressed" in event.action:
            bird.jump()
    bird.apply_gravity()

    if second_iteration:
        # Add new tubes
        if tubes[-1].get_x() < 3:
            tubes.append(TubeSet(randint(0, 5), 8, tube_color))

        # Move all tubes and remove redundant ones
        second_iteration = False
        tubes_to_remove = []

        for tube in tubes:
            if tube.get_x() < 0:
                tubes_to_remove.append(tube)
            tube.move(-1)

        # Remove redundant tubes
        for tube in tubes_to_remove:
            tubes.remove(tube)
    else:
        # Update on next iteration
        second_iteration = True

    # Draw the game
    game_matrix.fill_pixels(black)
    bird.draw(game_matrix)
    for tube in tubes:
        tube.draw(game_matrix)
    game_matrix.draw(sense)
