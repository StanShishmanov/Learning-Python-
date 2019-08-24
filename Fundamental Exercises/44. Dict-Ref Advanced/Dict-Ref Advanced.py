my_dict = {}
while True:
    line = input().split(' -> ')
    if line[0] == "end":
        break
    else:
        if line[1].isalpha():
            first_key = line[0]
            other_key = line[1]
            if other_key in my_dict.keys():
                if first_key not in my_dict.keys():
                    my_dict[first_key] = []
                else:
                    continue
                for v in my_dict[other_key]:
                    my_dict[first_key].append(v)
        else:
            my_key = line[0]
            digits = [i for i in line[1].split(', ')]
            if my_key not in my_dict.keys():
                my_dict[my_key] = []
                my_dict[my_key] = digits
            else:
                my_dict[my_key] += digits
for k, v in my_dict.items():
    print(f'{k} === {", ".join(v)}')
"""
Isacc -> 5, 4, 3
Peter -> 6, 3, 3
Derek -> 2, 2, 2

John -> Isacc
"""
