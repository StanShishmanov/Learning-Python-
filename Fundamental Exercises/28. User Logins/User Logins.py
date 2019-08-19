my_dict = {}
line = ""
count = 0
can_login = False
while True:
    line = input().split(' -> ')
    if line[0] == "end":
        break
    else:
        if line[0] == "login":
            can_login = True
        elif can_login == True:
            if line[0] in my_dict.keys():
                if my_dict[line[0]] == line[1]:
                    print(f'{line[0]}: logged in successfully')
                else:
                    print(f'{line[0]}: login failed')
                    count += 1
            elif (line[1] not in my_dict.keys()) or (line[1] != my_dict[line[0]]):
                print(f'{line[0]}: login failed')
                count += 1
        if can_login == False:
            if line[0] != "login":
                if line[0] in my_dict.keys():
                    my_dict[line[0]] = line[1]
                elif line[0] not in my_dict.keys():
                    my_dict[line[0]] = line[1]

print(f'unsuccessful login attempts: {count}')

