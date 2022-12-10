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
        self.__y_position += delta_y
