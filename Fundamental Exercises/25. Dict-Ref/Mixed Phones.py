my_dict = {}
while True:
    line = input().split(' : ')
    if line[0] == "Over":
        break
    else:
        if line[1].isdigit():
            my_dict[line[0]] = line[1]
        elif line[0].isdigit():
            my_dict[line[1]] = line[0]
for k, v in sorted(my_dict.items()):
    print(f'{k} -> {v}')