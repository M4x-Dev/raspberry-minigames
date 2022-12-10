class SenseMatrix:
    def __init__(self):
        self.__pixels = []

    def fill_pixels(self, value):
        self.__pixels = [value for _ in range(64)]

    def set_pixel(self, x, y, value):
        self.__pixels[SenseMatrix.x_and_y_to_absolute(x, y)] = value

    def get_pixels(self):
        return self.__pixels

    @staticmethod
    def x_and_y_to_absolute(x: int, y: int) -> int:
        return (y * 8) + (x % 8)
