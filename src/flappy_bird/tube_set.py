class TubeSet:
    def __init__(self, outlet_height, x_position, color):
        self.__outlet_height = outlet_height
        self.__x_position = x_position
        self.__color = color

    def draw(self, matrix):
        for x in range(2):
            for y in range(7):
                if y < self.__outlet_height or y > self.__outlet_height + 1:
                    if 0 <= self.__x_position + x <= 7 and 0 <= y <= 7:
                        matrix.set_pixel(self.__x_position + x, y, self.__color)

    def move(self, delta_x):
        self.__x_position += delta_x
