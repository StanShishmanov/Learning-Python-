def multiplication(num, input_list):
    return ' '.join(list(str(int(i) * num) for i in input_list))

print(multiplication(int(input()), input().split()))