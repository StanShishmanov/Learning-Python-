def sorter(input_list):
    total_sum = 0
    for i in input_list:
        if int(i) < 0:
            total_sum += int(i)
    return abs(total_sum)

print(sorter(input().split()))