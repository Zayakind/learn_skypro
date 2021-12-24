from homework21_labirint.terrain import Grass


class Cell:
    """Хранилище для объектов на игровом поле."""

    def __init__(self, obj):
        self.obj = obj

    def get_obj(self):
        """
        Возвращает объект из ячейки
        """

        return self.obj

    def set_obj(self, obj):
        """
        Меняет объект в ячейке
        """

        self.obj = obj


class Field:
    """Класс реализующий действия объектов на карте."""

    def __init__(self, field: list, unit, coord):
        self.field = field
        self.unit = unit
        self.coord = coord

    def cell(self, x, y):
        """
        Возвращаем объект на переданных координатах.
        """

        cell = self.field[x][y]
        return cell.get_obj()

    def _set_cell(self, obj, x, y):
        """
        Меняем объект на переданных координатах.
        """

        self.field[x][y].set_obj(obj)

    def move_unit_up(self):
        """
        Логика передвижения персонажа вверх.
        """

        x, y = self.unit.get_coordinates()
        cell = self.cell(x-1, y)
        if not cell.is_walkable:
            return print("Место не проходится, выберите другое направление")
        self.field[x][y].set_obj(Grass())
        cell.step_on(self.unit)
        if not self.unit.is_alive():
            return False
        self._set_cell(self.unit, x-1, y)
        coord = (x-1, y,)
        self.unit.set_coordinates(coord)

    def move_unit_down(self):
        """
        Логика передвижения персонажа вниз.
        """

        x, y = self.unit.get_coordinates()
        cell = self.cell(x+1, y)
        if not cell.is_walkable:
            return print("Место не проходится, выберите другое направление")
        self.field[x][y].set_obj(Grass())
        cell.step_on(self.unit)
        if not self.unit.is_alive():
            return False
        self._set_cell(self.unit, x+1, y)
        coord = (x+1, y,)
        self.unit.set_coordinates(coord)

    def move_unit_right(self):
        """
        Логика передвижения персонажа вправо.
        """

        x, y = self.unit.get_coordinates()
        cell = self.cell(x, y+1)
        if not cell.is_walkable:
            return print("Место не проходится, выберите другое направление")
        self.field[x][y].set_obj(Grass())
        cell.step_on(self.unit)
        if not self.unit.is_alive():
            return False
        self._set_cell(self.unit, x, y+1)
        coord = (x, y+1,)
        self.unit.set_coordinates(coord)

    def move_unit_left(self):
        """
        Логика передвижения персонажа влево.
        """

        x, y = self.unit.get_coordinates()
        cell = self.cell(x, y-1)
        if not cell.is_walkable:
            return print("Место не проходится, выберите другое направление")
        self.field[x][y].set_obj(Grass())
        cell.step_on(self.unit)
        self._set_cell(self.unit, x, y-1)
        coord = (x, y-1,)
        self.unit.set_coordinates(coord)

    def get_field(self):
        """
        Возвращает свойство field
        """
        return self.field
