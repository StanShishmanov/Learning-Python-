list_input = [int(i) for i in input().split(' ')]
i = 0
new_list = []
for i in range(len(list_input)):
    inserted = False
    j = 0
    for j in range(len(new_list)):
        if list_input[i] < new_list[j]:
            new_list.insert(j, list_input[i])
            inserted = True
            break
    if not inserted:
        new_list.append(list_input[i])
for i in new_list:
    print(f'{i}', end=" ")