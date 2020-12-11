def is_valid(number):
    min_num = 2
    max_num = 10
    # for i in range(min_num, max_num + 1):
    #     if number % i == 0:
    #         return True
    # return False
    results = [x for x in range(min_num, max_num + 1) if number % x == 0]
    return True if results else False


n = int(input())
m = int(input())

result = [x for x in range(n, m + 1) if is_valid(x)]
print(result)