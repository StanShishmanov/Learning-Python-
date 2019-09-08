monsters = []
num_hydras = 0
num_zerglings = 0
class Monster:
    def __init__(self, name, id, strength, ugliness):
        self.name = str(name)
        self.id = int(id)
        self.strength = int(strength)
        self.ugliness = int(ugliness)


class Zergling(Monster):
    def __init__(self, name, id, strength, ugliness, speed):
        Monster.__init__(self, name, id, strength, ugliness)
        self.speed = int(speed)


class Hydralisk(Monster):
    def __init__(self, name, id, strength, ugliness, range):
        Monster.__init__(self, name, id, strength, ugliness)
        self.range = str(range)


data = input()

while not data == "stopAddingArmy":
    data = data[:-1]
    monster = data.split('(')[0]
    name = data.split("'")[1]
    id = int(data.split(', ')[1])
    strength = int(data.split(', ')[2])
    ugliness = int(data.split(', ')[3])

    if monster == "Zergling":
        try:
            spec_attr = data.split(', ')[4]
            try:
                spec_attr = int(spec_attr)
                zergling = Zergling(name, id, strength, ugliness, spec_attr)
                monsters.append(zergling)
                num_zerglings += 1
            except Exception:
                print("Speed must be integer")

        except Exception:
            print("__init__() missing 1 required positional argument: 'speed'")


    if monster == "Hydralisk":
        try:
            spec_attr = data.split(', ')[4]
            try:
                spec_attr = spec_attr.replace("'","")
                if spec_attr.isalpha():
                    hydra = Hydralisk(name, id, strength, ugliness, spec_attr)
                    monsters.append(hydra)
                    num_hydras += 1
                else:
                    print("Range must be string")
            except Exception:
                print("Range must be string")


        except Exception:
            print("__init__() missing 1 required positional argument: 'range'")

    if monster == "BaseMonster":
        print("Can't instantiate abstract class BaseMonster with abstract methods __init__")
    data = input()
total_speed = 0
total_strength = 0
for i in monsters:
    total_strength += i.strength
    if isinstance(i, Zergling):
        total_speed += i.speed

print(f'Overall speed of army: {total_speed}')
print(f'Overall stength: {total_strength}')
print(f'Hydralisk: {num_hydras}; Zergling: {num_zerglings}')
""""

Zergling('Pesho', 10, 10, 10, 10)
Zergling('Pesho', 10, 10, 10, 20)
Hydralisk('a', 100, 100, 100, 'min')
Zergling('Pesho', 10, 10, 10, 30)
stopAddingArmy

Zergling('Pesho', 10, 10, 10, 10)
Zergling('Pesho', 10, 10, 10, 20)
Hydralisk('a', 100, 100, 100, 'min')
Zergling('Pesho', 10, 10, 10, 30)
stopAddingArmy

BaseMonster('A12', 150, 200, 300)
Zergling('Pesho', 10, 10, 10, 'min')
Hydralisk('a', 100, 100, 100, 10)
Zergling('Pesho', 10, 10, 10)
Hydralisk('a', 100, 100, 100)
stopAddingArmy


"""



