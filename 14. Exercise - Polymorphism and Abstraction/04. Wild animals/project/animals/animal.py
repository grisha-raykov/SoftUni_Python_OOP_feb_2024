from abc import ABC, abstractmethod





class Animal(ABC):

    def __init__(self, name: str, weight: float):
        self._name = name
        self._weight = weight
        self._food_eaten = 0

    @property
    def name(self):
        return self._name

    @property
    def weight(self):
        return self._weight

    @property
    def food_eaten(self):
        return self._food_eaten

    @weight.setter
    def weight(self, value):
        self._weight = value

    @food_eaten.setter
    def food_eaten(self, value):
        self._food_eaten = value

class Bird(Animal, ABC):

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self._wing_size = wing_size

    @property
    def wing_size(self):
        return self._wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"

class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self._living_region = living_region

    @property
    def living_region(self):
        return self._living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"