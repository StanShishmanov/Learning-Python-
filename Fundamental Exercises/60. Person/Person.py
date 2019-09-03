class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 3:
            raise Exception("Name's length should not be less than 3 symbols!")
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if int(age) < 0:
            raise Exception('Age must be positive!')
        elif int(age) > 15:
            raise Exception("Child's age must be less than 15!")
        else:
            self.__age = age

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'


class Child(Person):

    def __init__(self, name, age):
        Person.__init__(self, name, age)


name = input()
age = int(input())
try:
    child = Child(name, age)
    print(child)
except Exception as exe:
    print(exe)