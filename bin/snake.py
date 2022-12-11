from src.sense_matrix import SenseMatrix
from sense_hat import SenseHat
from time import sleep

snake_color = [0, 0, 190]
food_color = [190, 0, 0]
black = [0, 0, 0]

sense = SenseHat()
game_matrix = SenseMatrix()

snake = [[0, 0]]
snake_velocity = [1, 0]
food = [7, 7]

while True:
    # Reduce the game speed
    sleep(0.25)

    # Detect joystick events and update velocity
    for event in sense.stick.get_events():
        if "pressed" in event.action:
            if "up" in event.direction:
                snake_velocity = [0, -1]
            elif "down" in event.direction:
                snake_velocity = [0, 1]
            elif "left" in event.direction:
                snake_velocity = [-1, 0]
            elif "right" in event.direction:
                snake_velocity = [1, 0]

    # Update the snake body
    snake.insert(0, [snake[0][0] + snake_velocity[0], snake[0][1] + snake_velocity[1]])
    if snake[0] == food[0] and snake[1] == food[1]:
        pass
    else:
        snake.pop()

    # Draw the snake and the food
    for coordinates in snake:
        game_matrix.set_pixel(coordinates[0], coordinates[1], snake_color)
    game_matrix.set_pixel(food[0], food[1], food_color)
    game_matrix.draw(sense)
