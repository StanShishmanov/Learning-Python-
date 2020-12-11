from abc import ABC, abstractmethod

from project.animals.animal import Animal


class Mammal(Animal, ABC):

    food_eaten = 0

    def __init__(self, name: str, weight: float, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    @abstractmethod
    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Mouse(Mammal):

    food_eaten = 0

    def __init__(self, name: str, weight: float, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if "Fruit" != food.__class__.__name__ or "Vegetable" != food.__class__.__name__:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.10

    def __repr__(self):
        return super().__repr__()


class Dog(Mammal):

    food_eaten = 0

    def __init__(self, name: str, weight: float, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if "Meat" != food.__class__.__name__:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.40

    def __repr__(self):
        return super().__repr__()


class Cat(Mammal):

    food_eaten = 0

    def __init__(self, name: str, weight: float, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if "Meat" != food.__class__.__name__ or "Vegetable" != food.__class__.__name__:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.30

    def __repr__(self):
        return super().__repr__()


class Tiger(Mammal):

    food_eaten = 0

    def __init__(self, name: str, weight: float, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if "Meat" != food.__class__.__name__:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * 1.00

    def __repr__(self):
        return super().__repr__()