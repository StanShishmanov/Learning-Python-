data = input().split()
while not data[0] == "stop":
    unique = False
    my_list = []
    new_list = []
    for i in data:
        my_list.append(int(i))
    if len(my_list) == len(set(my_list)):
        unique = True
        for i in my_list:
            if i % 2 == 0:
                new_list.append(i + 2)
            else:
                new_list.append(i)
    else:
        for i in my_list:
            if i % 2 != 0:
                new_list.append(i + 3)
            else:
                new_list.append(i)
    index = 1
    while index != len(new_list):
        previous = new_list[index - 1]
        current = new_list[index]
        if previous > current:
            to_switch = new_list[index]
            new_list[index] = previous
            new_list[index - 1] = to_switch
            index = 0
        index += 1

    sum_all = sum(new_list)
    length = len(new_list)
    output = float(sum_all / length)
    if unique:
        #for i in new_list:
        print(f"Unique list: {','.join(map(str, new_list))}")
        print(f'Output: {output:.2f}')
    else:
        print(f"Non-unique list: {':'.join(map(str, new_list))}")
        print(f'Output: {output:.2f}')

    data = input().split()




""""
1 2  3   4 5 6
1 1 2   2 1 4 7 7 8 8 
 5 5 5 5
"""