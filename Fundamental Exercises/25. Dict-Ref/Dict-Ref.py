my_dict = {}
while True:
    line = input().split(' = ')
    if line[0] == "end":
        break
    else:
        if line[1].isdigit():
            my_dict[line[0]] = int(line[-1])

        elif line[1] in my_dict.keys():
            my_dict[line[0]] = my_dict[line[1]]
for k, v in my_dict.items():
    print(f'{k} === {v}')
