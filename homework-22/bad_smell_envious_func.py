class Cube:

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def get_coordinates(self) -> int:
        return self.x * self.y * self.z


class CubeVolumeCalculator:

    @staticmethod
    def calc_cube_volume(cube):
        return cube.get_coordinates()
