n = [int(i) for i in input().split()]
sqr_num = 0.5
new_list = []
for i in n:
    if i ** sqr_num == int(i ** sqr_num):
        new_list.append(i)
new_list.sort(reverse=True)
for i in new_list:
    print(f'{i}', end=" ")