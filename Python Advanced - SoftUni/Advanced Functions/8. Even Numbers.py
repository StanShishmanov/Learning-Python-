nums_input = [int(i) for i in input().split()]

even_nums = filter(lambda x: int(x) % 2 == 0, nums_input)

print(list(even_nums))