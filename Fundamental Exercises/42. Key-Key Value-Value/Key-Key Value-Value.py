key_input = input()
value_input = input()
n = int(input())
my_dict = {}
i = 0
while i < n:

    dict_input = input().split(' => ')
    my_key = dict_input[0]
    list_values = dict_input[1].split(";")
    my_dict = {my_key:list_values}

    for k, v in my_dict.items():
        if key_input in k:
            print(f'{k}:')
            for v in my_dict[k]:
                if value_input in v:
                    print(f'-{v}')
    i += 1
