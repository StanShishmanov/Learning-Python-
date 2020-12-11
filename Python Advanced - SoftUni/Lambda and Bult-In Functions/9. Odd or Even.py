def odd_even_multiplier(*args):
    command = args[0]
    nums_list = [i for i in args[1:][0]]
    if command == "Odd":
        return sum(list(filter(lambda x: x % 2 == 1, nums_list))) * len(nums_list)
    return sum(filter(lambda x: x % 2 == 0, nums_list)) * len(nums_list)

print(odd_even_multiplier(input(), [int(x) for x in input().split()]))