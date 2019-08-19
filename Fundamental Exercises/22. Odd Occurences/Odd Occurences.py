my_list = input().lower().split(' ')
my_dict = {}
for i in my_list:
    count = my_list.count(i)
    if count % 2 != 0:
        my_dict[i] = count
print(f"{', '.join(my_dict.keys())}")