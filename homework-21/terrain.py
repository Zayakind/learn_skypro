import random


class Terrain:
    """Родительский класс для формирования игрового поля."""

    def __init__(self, terrain, is_walkable):
        self.is_walkable = is_walkable
        self.terrain = terrain

    def step_on(self, unit):
        """
        Шаблон для поведения когда наступили на террейн.
        :param unit:
        """
        pass

    def is_walkable(self) -> bool:
        """
        Флаг проходимости объекта.
        """

        return self.is_walkable()

    def get_terrain(self) -> str:
        """
         Возвращает имя объекта.
        """

        return self.terrain


class Grass(Terrain):
    """Террайн травы, проходимый."""

    def __init__(self):
        super().__init__(terrain='Grass', is_walkable=True)


class Wall(Terrain):
    """Террайн стены, проходимый."""

    def __init__(self):
        super().__init__(terrain='Wall', is_walkable=False)


class Door(Terrain):
    """Класс двери, проверящий наличие ключа у игрока и если есть, переворачивает флаг escaped."""

    def __init__(self, terrain='Door', is_walkable=True):
        super().__init__(terrain, is_walkable)
        self.terrain = terrain

    def step_on(self, unit):
        """
        Проверяет есть ли у игрока ключ и если да, открывает дверь.
        """
        if unit.has_key():
            unit.escaped = True


class Key(Terrain):
    """Объект ключа, при нахождении игроком меняет флаг got_key."""

    def __init__(self, terrain='Key', is_walkable=True):
        super().__init__(terrain, is_walkable)
        self.terrain = terrain

    def step_on(self, unit):
        """
        Меняет состояние ключа у Персонажа на True.
        """
        unit.set_key()


class Trap(Terrain):
    """Террайн ловушки, наносит урон персонажу, проходимый."""

    def __init__(self, terrain='Trap', is_walkable=True):
        super().__init__(terrain, is_walkable)
        self.terrain = terrain

    def damage(self):
        """
        Высчитывает урон.
        """
        damage = random.choice(range(15, 20))
        return damage

    def step_on(self, unit):
        """
        Наносит урон персонажу
        """
        unit.get_damage(unit, self.damage())
