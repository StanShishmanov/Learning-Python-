my_list = [int(i) for i in input().split(" ")]
new_list = []
counter = 0
for i in my_list:
    if i < 0:
        counter += 1
if counter == len(my_list):
    print('empty')
else:
    for i in my_list:
        if i > 0:
            new_list.append(i)
    if len(my_list) != 0:
        for i in new_list[::-1]:
            print(f"{i}", end=" ")