class Animal:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


#
# lizard = Lizard("John")
# print(lizard.__class__.__bases__[0].__name__)
# print(lizard.name)
# print(lizard._Animal__name)	Animal
# Stella
# Stella
# Reptile
# John
# John
