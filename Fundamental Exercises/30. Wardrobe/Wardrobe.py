n = int(input())
my_dict = {}
for i in range(n):
    line = input().split(' -> ')
    value_list = list(line[1].split(','))
    key_one = line[0]
    if key_one not in my_dict.keys():
        my_dict[key_one] = {}
        for i in value_list:
            if i not in my_dict[key_one].keys():
                my_dict[key_one][i] = 1
            else:
                my_dict[key_one][i] += 1
    else:
        for i in value_list:
            if i not in my_dict[key_one].keys():
                my_dict[key_one][i] = 1
            else:
                my_dict[key_one][i] += 1

last_input = input().split(' ')
input_key = last_input[0]
second_key = last_input[1]

for i in my_dict.keys():
    print(f'{i} clothes:')
    for k,v in my_dict[i].items():
        if i == input_key and k == second_key:
            print(f'* {k} - {v} (found!)')
        else:
            print(f'* {k} - {v}')