class Unit:
    """Шаблон для создания персонажей."""

    def __init__(self, hp: int, coord: tuple, got_key=False, escaped=False):
        self.hp = hp
        self.got_key = got_key
        self.coord = coord
        self.escaped = escaped

    def has_key(self) -> bool:
        """
        Возвращает состояние ключа.
        """

        if self.got_key:
            return True

    def set_key(self):
        """
        Меняет состояние ключа.
        """

        print("Вы нашли ключ от двери!")
        self.got_key = True

    def has_escaped(self) -> bool:
        """
        Проверяет вышел ли персонаж.
        """

        if self.escaped:
            return True

    def is_alive(self) -> bool:
        """
        Проверяет положительное ли количество хитпоинтов.
        """
        if self.hp > 0:
            return True
        else:
            print('You dead!')
            return False

    def get_damage(self, unit, damage):
        """
        Обрабатывает входящий урон.
        :param unit:
        :param damage:
        """
        unit.hp -= damage

    def set_coordinates(self, coord: tuple):
        """
        Устанавливает координаты юнита.
        :param coord: Будущие координаты.
        """
        self.coord = coord

    def get_coordinates(self) -> tuple:
        """
        Возвращает координаты юнита.
        :return: текущие координаты Персонажа.
        """
        return self.coord

    def has_position(self, coord: tuple) -> True:
        """
        Проверяет в этих ли координатах юнит.
        :param coord:
        """
        if coord == self.coord:
            return True


class Ghost(Unit):
    """Игровой персонаж."""

    def __init__(self, hp: int, coord):
        super().__init__(hp, coord)
        self.terrain = 'Ghost'

