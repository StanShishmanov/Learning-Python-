my_dict = {}
can_stock = True
can_buy = False
while True:
    line = input().split(' ')
    if line[0] == 'exam':
        break
    elif line[0] == "stock":
        if can_stock == True:
            if line[0] == "stock":
                if line[1] not in my_dict.keys():
                    my_dict[line[1]] = int(line[2])
                else:
                    my_dict[line[1]] += int(line[2])
    elif line[0] == "shopping":
        can_stock = False
        can_buy = True
    elif can_buy == True:
        if line[0] == "buy":
            if line[1] in my_dict.keys():
                if my_dict[line[1]] > 0:
                    if my_dict[line[1]] < int(line[2]):
                        my_dict[line[1]] = int(0)
                    elif my_dict[line[1]] >= int(line[2]):
                        my_dict[line[1]] -= int(line[2])
                elif my_dict[line[1]] == 0:
                    print(f"{line[1]} out of stock")
            else:
                print(f"{line[1]} doesn't exist")
for k, v in my_dict.items():
    if my_dict[k] > 0:
        print(f'{k} -> {v}')