def unique_name_printer(input_list):
    new_list = list(filter(lambda x: x[0].isupper() and x[1:].islower(), input_list))
    total_sum = 0
    for name in new_list:
        total_sum += len(name)
    return total_sum

print(unique_name_printer(input().split()))