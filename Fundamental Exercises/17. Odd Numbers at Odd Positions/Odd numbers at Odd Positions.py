my_list = [int(i) for i in input().split(" ")]
new_list = []
for index, odd in enumerate(my_list):
    if index % 2 != 0:
        if odd % 2 != 0:
            print(f'Index {index} -> {odd}', end="\n")