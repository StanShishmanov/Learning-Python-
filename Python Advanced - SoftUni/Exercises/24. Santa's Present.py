from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])
presents = {
    "Bicycle": 0,
    "Doll": 0,
    "Teddy bear" : 0,
    "Wooden train" : 0
}
doll = 150
wooden_train = 250
teddy_bear = 300
bicycle = 400

while True:
    if not materials:
        break
    elif not magic_level:
        break
    else:
        material = materials.pop()
        magic = magic_level.popleft()
        multi = material * magic
        if multi == doll:
            presents["Doll"] += 1
        elif multi == wooden_train:
            presents["Wooden train"] += 1
        elif multi == teddy_bear:
            presents["Teddy bear"] += 1
        elif multi == bicycle:
            presents["Bicycle"] += 1
        else:
            if multi < 0:
                material += magic
                materials.append(material)
            elif multi > 0:
                materials.append(material + 15)
            else:
                if not material == 0:
                    materials.append(material)
                if not magic == 0:
                    magic_level.appendleft(magic)

sorted_presents = sorted(presents.items())
for key, value in presents.items():
    if (presents["Doll"] > 0 and presents["Wooden train"] > 0) or (presents["Bicycle"] > 0 and presents["Teddy bear"] > 0):
        print(f"The presents are crafted! Merry Christmas!")
        break
    else:
        print('No presents this Christmas!')
        break
if materials:
    print(f"Materials left: " + ', '.join(map(str, materials[::-1])))
if magic_level:
    print(f"Magic left: " + ', '.join(map(str, magic_level)))
    
for i in sorted_presents:
    if i[1] > 0:
        print(f'{i[0]}: {i[1]}')