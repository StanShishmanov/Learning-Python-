list_input = [int(i) for i in input().split(' ')]
n = int(input())
list_input = sorted(list_input, reverse= True)
i = 0
j = 0
for i in list_input:
    j += 1
    if j > n:
        break
    else:
        print(f'{i}', end=" ")