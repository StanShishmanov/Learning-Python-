n = [x for x in input().split(" ")]
new_list = []
for i in n:
    if i == n[-1]:
        new_list.insert(0, i)
    else:
        new_list.append(i)
print(f'{" ".join(new_list)}', end=" ")