import re
travel_dict = {}
while True:
    my_input = input().split(':')
    if my_input[0] == "ready":
        break
    else:
        kv_pairs_list = re.split('[,-]+', my_input[1])
        city_key = my_input[0]
        if city_key not in travel_dict:
            travel_dict[city_key] = {}
        i = 0
        for i in range(len(kv_pairs_list)):
            if i % 2 == 0:
                key = kv_pairs_list[i]
                value = kv_pairs_list[i + 1]
                travel_dict[city_key][key] = int(value)
while True:
    my_input_1 = input().split(' ')
    if my_input_1[0] == "travel":
        break
    else:
        city_key_1 = my_input_1[0]
        people = int(my_input_1[1])
        total = 0
        for v in travel_dict[city_key_1].values():
            total += v
        if people > total:
            over_limit = people - total
            print(f'{city_key_1} -> all except {over_limit} accommodated')
        else:
            print(f'{city_key_1} -> all {people} accommodated')