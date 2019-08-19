import math
crab_dict = {}
shell_list = []
list_average = 0
can_input = True
while can_input:
    shell_input = input().split(' ')
    if len(shell_input) > 1:
        region = shell_input[0]
        shell_quantity = int(shell_input[1])
    else:
        can_input = False
        break
    if region not in crab_dict.keys():
        crab_dict[region] = []
        if shell_quantity not in crab_dict[region]:
            crab_dict[region].append(int(shell_quantity))
    else:
        if shell_quantity not in crab_dict[region]:
            crab_dict[region].append(int(shell_quantity))

for i in crab_dict.keys():
    for j in i:
        sum_of_shells = float(sum(crab_dict[i]))
        list_average = sum_of_shells - (sum_of_shells / float(len(crab_dict[i])))
    crab_dict[i].append(math.ceil(list_average))

for k, v in crab_dict.items():
    print(f'{k} -> {", ".join(map(str, v[:-1]))} ({v[-1]})', sep=" ")