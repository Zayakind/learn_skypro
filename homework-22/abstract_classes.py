from abc import ABC, abstractmethod


class Transport(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Boat(Transport):

    def start_engine(self):
        print("Start Engine Boat")

    def stop_engine(self):
        print("Stop Engine Boat")

    def move(self):
        print("Move Boat")

    def stop(self):
        print("Stop Boat")


class Car(Transport):

    def start_engine(self):
        print("Start Engine Car")

    def stop_engine(self):
        print("Stop Engine Car")

    def move(self):
        print("Move Car")

    def stop(self):
        print("Stop Car")


class Electroscooter(Transport):

    def start_engine(self):
        print("Start Engine Electroscooter")

    def stop_engine(self):
        print("Stop Engine Electroscooter")

    def move(self):
        print("Move Electroscooter")

    def stop(self):
        print("Stop Electroscooter")


class Person:

    def use_transport(self, transport: Transport):
        transport.start_engine()
        transport.move()
        transport.stop()
        transport.stop_engine()