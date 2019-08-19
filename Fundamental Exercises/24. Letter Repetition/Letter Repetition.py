my_list = input()
my_dict = {}
for i in my_list:
    count = my_list.count(i)
    my_dict[i] = count
for key, value in my_dict.items():
    print(f'{key} -> {value}')