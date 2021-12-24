class Room:

    def get_name(self):
        print(42)
        return 42


class Street:

    def get_room(self) -> int:
        return Room().get_name()


class City:

    def get_street(self) -> int:
        return Street().get_room()

    def population(self):
        print(100500)
        return 100500


class Country:

    def get_city(self) -> int:
        return City().get_street()


class Planet:

    def get_contry(self, data) -> int:
        if data == 'room':
            return Country().get_city()
        if data == 'population':
            return City().population()


class Person:
    def __init__(self):
        self.planet = Planet()

    def get_person(self, data):
        return self.planet.get_contry(data)


if __name__ == '__main__':
    person = Person()
    person.get_person('room')
    person.get_person('population')
