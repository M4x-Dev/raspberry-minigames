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
    # Reduce the game speed
    sleep(0.25)

    # Detect joystick events
    for event in sense.stick.get_events():
        if "up" in event.direction and "pressed" in event.action:
            player_wall.move(-1)
        elif "down" in event.direction and "pressed" in event.action:
            player_wall.move(1)

    # Move the computer wall
    computer_wall.apply_y(ball[1])

    # Collision detection
    if (ball[1] == 0 and ball_velocity[1] < 0) or (ball[1] == 7 and ball_velocity[1] > 0):
        ball_velocity[1] = -ball_velocity[1]
    if (ball[0] == 0 and ball_velocity[0] < 0) or (ball[0] == 7 and ball_velocity[0] > 0):
        ball_velocity[0] = -ball_velocity[0]

    # Move the ball
    for i in range(len(ball)):
        ball[i] += ball_velocity[i]

    # Draw the game
    game_matrix.fill_pixels(black)
    game_matrix.set_pixel(ball[0], ball[1], game_color)
    player_wall.draw(game_matrix)
    computer_wall.draw(game_matrix)
    game_matrix.draw(sense)
