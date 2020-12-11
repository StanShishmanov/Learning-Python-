def round_and_multiply(input_list):
    total_sum = 0
    for i in input_list:
        total_sum += round(float(i))
    return total_sum * len(input_list)

print(round_and_multiply(input().split()))