class Animal:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 1:
            raise Exception("Invalid input!")
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if int(age) < 0:
            raise Exception("Invalid input!")
        self.__age = age

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        if len(gender) < 0:
            raise Exception("Invalid input!")
        self.__gender = gender


    def produce_sound(self):
        return f""

    def __str__(self):
        return f"{typeof(self)}\n{self.name} {self.age} {self.gender}\n{self.produce_sound()}"


class Dog(Animal):
    def __init__(self, name, age, gender):
        Animal.__init__(self, name, age, gender)

    def produce_sound(self):
        return f'Woof!'


class Frog(Animal):
    def __init__(self, name, age, gender):
        Animal.__init__(self, name, age, gender)


    def produce_sound(self):
        return f'Ribbit'


class Cat(Animal):
    def __init__(self, name, age, gender):
        Animal.__init__(self, name, age, gender)


    def produce_sound(self):
        return f'Meow meow'


class Kitten(Cat):
    def __init__(self, name, age, gender=None):
        Cat.__init__(self, name, age, gender)
        self.gender = "Female"
    def produce_sound(self):
        return f'Meow'


class Tomcat(Cat):
    def __init__(self, name, age, gender=None):
        Cat.__init__(self, name, age, gender)
        self.gender = "Male"

    def produce_sound(self):
        return f'MEOW'


animals = []
classes = ['Animal', 'Dog', 'Cat', 'Frog', 'Kitten', 'Tomcat']
while True:
    cls = input()
    if cls == "Beast!":
        break

    else:

        data_two = input().split()
        name = data_two[0]
        age = data_two[1]
        gender = data_two[2]
        if cls not in classes:
            print('Invalid input!')
            continue
        try:
            string = f'{cls} ("{name}", {age}, "{gender}")'
            obj = eval(string)
            animals.append(obj)
        except Exception as exe:
            print(exe)

for i in animals:
    print(type(i).__name__)
    print(f'{i.name} {i.age} {i.gender}')
    print(f'{i.produce_sound()}')