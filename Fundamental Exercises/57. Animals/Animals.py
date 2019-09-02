animals = []
dogs = []
cats = []
snakes = []
class Dog:
    def __init__(self, name, age, number_of_legs):
        self.name = name
        self.age = age
        self.num_legs = number_of_legs

    def produce_sound(self):
        print("I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.")


class Cat:
    def __init__(self, name, age, intelligence_quotient):
        self.name = name
        self.age = age
        self.int_quot = intelligence_quotient

    def produce_sound(self):
        print("I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau.")


class Snake:
    def __init__(self, name, age, cruelty_coefficient):
        self.name = name
        self.age = age
        self.cr_coeff = cruelty_coefficient

    def produce_sound(self):
        print("I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home.")

data = input()
while not data == "I'm your Huckleberry":
    command = data.split(' ')[0]
    name = data.split(' ')[1]
    if command == "talk":
        for animal in animals:
            if animal.name == name:
                animal.produce_sound()
    else:

        age = data.split(' ')[2]
        param = data.split(' ')[3]

        if command == "Dog":
            animal_class = Dog(name, age, param)
            dogs.append(animal_class)
            animals.append((animal_class))
        elif command == "Cat":
            animal_class = Cat(name, age, param)
            cats.append(animal_class)
            animals.append((animal_class))
        else:
            animal_class = Snake(name, age, param)
            snakes.append(animal_class)
            animals.append((animal_class))
    data = input()

for dog in dogs:
    print(f'Dog: {dog.name}, Age: {dog.age}, Number Of Legs: {dog.num_legs}')
for cat in cats:
    print(f'Cat: {cat.name}, Age: {cat.age}, IQ: {cat.int_quot}')
for snake in snakes:
    print(f'Snake: {snake.name}, Age: {snake.age}, Cruelty: {snake.cr_coeff}')


""""
Dog Sharo 3 4
Cat Garfield 5 200
Snake Alex 25 1000
talk Sharo
talk Garfield
talk Alex
I'm your Huckleberry
"""