class Wall:
    def __init__(self, height, x_position, color):
        self.__height = height
        self.__x_position = x_position
        self.__y_position = 2
        self.__color = color

    def draw(self, matrix):
        for y in range(self.__height):
            matrix.set_pixel(self.__x_position, self.__y_position + y, self.__color)

    def move(self, delta_y):
        if delta_y < 0 and self.__y_position > 0:
            self.__y_position += delta_y
        elif delta_y > 0 and self.__y_position < (8 - self.__height):
            self.__y_position += delta_y
