text = input()

my_list = []
for i in text:
    my_list.append(i)
my_list.sort()
my_set = set(my_list)
for i in my_list:
    if i in my_set:
        print(f'{i}: {my_list.count(i)} time/s')
        my_set.discard(i)