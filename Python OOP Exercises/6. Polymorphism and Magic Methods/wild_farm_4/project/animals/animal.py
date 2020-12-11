from abc import ABC, abstractmethod


class Animal(ABC):

    food_eaten = 0

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass


#

# # #
# hen = Hen("Harry", 10, 10)
# veg = Vegetable(3)
# fruit = Fruit(5)
# meat = Meat(1)
# print(hen)
# print(hen.make_sound())
# hen.feed(veg)
# hen.feed(fruit)
# hen.feed(meat)
# print(hen)
