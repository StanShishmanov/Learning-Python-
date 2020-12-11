def rounder(input_nums=[]):
    new_list = []
    for i in input_nums:
        new_list.append(round(float(i)))
    return new_list

print(rounder(input().split()))