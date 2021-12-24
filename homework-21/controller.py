from homework21_labirint.fields import Field, Cell
from homework21_labirint.hero import Ghost
from homework21_labirint.terrain import Grass, Wall, Trap, Key, Door


class GameController:
    """Класс объединяющий в себе всю игровую логику"""

    def __init__(self):
        self.mapping = {
            'Wall': '🔲',
            'Grass': '⬜',
            'Ghost': '👻',
            'Key': '🗝',
            'Door': '🚪',
            'Trap': '💀',
        }
        self.game_on = True
        self.hero = None
        self.field = None

    # Метод для назначения типа тиррейна по имени из строки lvlstring
    def _make_cell_terrain(self, name, *args, **kwargs):
        if name == 'W':
            return Cell(Wall())

        if name == 'g':
            return Cell(Grass())

        if name == 'T':
            return Cell(Trap())

        if name == 'G':
            self.hero = Ghost(25, *args, **kwargs)
            return Cell(Ghost(25, *args, **kwargs))

        if name == 'K':
            return Cell(Key())

        if name == 'D':
            return Cell(Door())

    # Метод для отрисовки карты в консоли
    def _draw_field(self):
        for cols in self.field.field:
            for rows in cols:
                print(f"{self.mapping.get(rows.get_obj().terrain)}", end=' ')
            print()

    # Метод создающий пустой шаблон карты
    def _get_matrix(self, lvlstring):
        area = []
        for line in lvlstring.split("\n"):
            line = line.strip()
            cell_line = []
            for square in line:
                cell_line.append(square)
            area.append(cell_line)
        return area

    # Метод для заполнения карты объектами и отрисовки в консоли
    def make_field(self, lvlstring):
        game_field = self._get_matrix(lvlstring)
        for cols in range(len(game_field)):
            for rows in range(len(game_field[cols])):
                coord = (cols, rows,)
                cell_obj = game_field[cols][rows]
                game_field[cols][rows] = self._make_cell_terrain(cell_obj, coord)
        self.field = Field(game_field, self.hero, self.hero.get_coordinates())
        self._draw_field()

    # Метод для начала игры и взаимодействия с игроком
    def play(self):

        while self.game_on and not self.hero.escaped:
            print("Добро пожаловать в игру, введите пожалуйста направление для движения: "
                  "w - вверх, a - влево, s - вниз, d - вправо\n"
                  "Вы можете выйти с помощью команд - stop/exit")
            command = input()
            if command == 'stop' or command == 'exit':
                self.game_on = False
                break
            if command == 'w':
                self.field.move_unit_up()
                if not self.hero.is_alive():
                    self.game_on = False
                    break
                self._draw_field()
            if command == 'a':
                self.field.move_unit_left()
                if not self.hero.is_alive():
                    self.game_on = False
                    break
                self._draw_field()
            if command == 's':
                self.field.move_unit_down()
                if not self.hero.is_alive():
                    self.game_on = False
                    break
                self._draw_field()
            if command == 'd':
                self.field.move_unit_right()
                if not self.hero.is_alive():
                    self.game_on = False
                    break
                self._draw_field()
        else:
            print('Game Over')
