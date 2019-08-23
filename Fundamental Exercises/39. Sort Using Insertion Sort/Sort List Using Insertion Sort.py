list_input = [int(i) for i in input().split(' ')]
i = 1
while i < len(list_input):
    j = i
    if j > 0 and list_input[j - 1] > list_input[j]:
        hold = list_input[j - 1]
        list_input[j - 1] = list_input[j]
        list_input[j] = hold
        i = 1
    else:
        i += 1
for i in list_input:
    print(f'{i}', end=" ")