input_list = [int(i) for i in input().split(' ')]
input_list.sort()
i = 0
count = 1
while i < len(input_list):
    if len(input_list) == 1:
        print(f'{input_list[0]} -> {count}')
        break
    else:
        current = input_list[i]
        next_num = input_list[i + 1]
        if current == next_num:
            count += 1
            input_list.remove(input_list[0])
            if len(input_list) == 1:
                print(f'{input_list[0]} -> {count}')
                break
        else:
            print(f'{input_list[0]} -> {count}')
            input_list.remove(input_list[0])
            i = 0
            count = 1
#8 2 2 8 2 2 3 7
#2 5 -3 7 -8 4 4 -8 3 5