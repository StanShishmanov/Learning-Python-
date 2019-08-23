int_list = [int(i) for i in input().split(' ')]
reversed_list = int_list[::-1]
for i in reversed_list:
    print(f'{i}', end=" ")