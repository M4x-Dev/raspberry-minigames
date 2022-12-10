from src.sense_matrix import SenseMatrix
from sense_hat import SenseHat

sense = SenseHat()
white = [255, 255, 255]

matrix = SenseMatrix()
matrix.fill_pixels([0, 0, 0])
matrix.set_pixel(0, 0, white)
matrix.set_pixel(0, 7, white)
matrix.set_pixel(7, 0, white)
matrix.set_pixel(7, 7, white)
sense.set_pixels(matrix.get_pixels())
