from abc import ABC, abstractmethod

from project.animals.animal import Animal
from project.food import Meat, Vegetable, Fruit


class Bird(Animal, ABC):

    food_eaten = 0

    def __init__(self, name: str, weight: float, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    @abstractmethod
    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Owl(Bird):

    food_eaten = 0

    def __init__(self, name: str, weight: float, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if "Meat" != food.__class__.__name__:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.25

    def __repr__(self):
        return super().__repr__()


class Hen(Bird):

    food_eaten = 0

    def __init__(self, name: str, weight: float, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.35

    def __repr__(self):
        return super().__repr__()


owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
# print(meat.__class__.__name__)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)