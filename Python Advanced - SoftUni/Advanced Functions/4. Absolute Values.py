def absolute(input_nums=[]):
    new_list = []
    for i in input_nums:
        new_list.append(abs(float(i)))
    return new_list

print(absolute(input().split()))