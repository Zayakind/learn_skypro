class Cube:
    x: int
    y: int
    z: int

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z


class CubeVolumeCalculator:

    @staticmethod
    def calc_cube_volume(cube):
        return cube.get_x() * cube.get_y() * cube.get_y()
