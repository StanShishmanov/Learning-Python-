elements = input().split()
elements = [int(i) for i in elements]

data = input()
game_rounds = 0
while not data == "exhausted":
    if data == "set":
        game_rounds += 1
        if len(set(elements)) == len(elements):
            print("It is a set")
        else:
            new_list = sorted(set(elements), key=elements.index)
            print(new_list)
    elif "filter" in data:
        game_rounds += 1
        command = data.split()[1]
        if command == "even":
            new_list = [i for i in elements if i % 2 == 0]
        else:
            new_list = [i for i in elements if i % 2 != 0]
        if len(new_list) == 0:
            break
        else:
            print(new_list)
    elif "multiply" in data:
        game_rounds += 1
        multiplier = int(data.split()[1])
        new_list = [x * multiplier for x in elements]
        print(new_list)
    elif "divide" in data:
        game_rounds += 1
        divider = int(data.split()[1])
        if divider == 0:
            print("ZeroDivisionError caught")
        else:
            new_list = [x / divider for x in elements]
            print(new_list)
    elif "slice" in data:
        game_rounds += 1
        index_1 = int(data.split()[1])
        index_2 = int(data.split()[2])
        if index_1 < 0 or index_2 < 0:
            print("IndexError caught")
        elif index_1 > (len(elements) - 1) or index_2 > (len(elements) - 1):
            print("IndexError caught")
        else:
            print(elements[index_1:index_2+1])
    elif "sort" in data:
        game_rounds += 1
        new_list = sorted(elements, key=lambda x: x)
        new_list.sort()
        print(new_list)
    elif "reverse" in data:
        game_rounds += 1
        new_list = elements[::-1]
        print(new_list)
    data = input()
print(f'I beat It for {game_rounds} rounds!')