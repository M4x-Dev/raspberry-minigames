class Bird:
    def __init__(self, x_position, y_position, color):
        self.__x_position = x_position
        self.__y_position = y_position
        self.__y_velocity = 1
        self.__color = color

    def get_x(self):
        return self.__x_position

    def get_y(self):
        return self.__y_position

    def normalized_velocity(self):
        if self.__y_velocity < 0:
            return -1
        elif self.__y_velocity > 0:
            return 1
        else:
            return 0

    def apply_gravity(self):
        if self.__y_velocity < 1:
            self.__y_velocity += 1

    def jump(self):
        self.__y_velocity = -3

    def draw(self, matrix):
        if 0 <= self.__y_position + self.normalized_velocity() <= 7:
            self.__y_position += self.normalized_velocity()

        matrix.set_pixel(self.__x_position, self.__y_position, self.__color)
