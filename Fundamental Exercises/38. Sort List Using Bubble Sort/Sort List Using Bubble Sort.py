list_input = [int(i) for i in input().split(' ')]
temp = False

while not temp:
    temp = True
    for i in range(len(list_input) - 1):
        if list_input[i] > list_input[i + 1]:
            temp = False
            hold = list_input[i + 1]
            list_input[i + 1] = list_input[i]
            list_input[i] = hold
for i in list_input:
    print(f'{i}', end=" ")