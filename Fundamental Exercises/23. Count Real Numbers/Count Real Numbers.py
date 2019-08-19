my_list = list(map(float, input().split(' ')))
my_dict = {}
for i in my_list:
    count = my_list.count(i)
    my_dict[i] = count
for key, value in sorted(my_dict.items()):
    print(f"{key} -> {value} times")