def recursive_power(num, count):
    if count == 1:
        return num
    return num * recursive_power(num, count - 1)

print(recursive_power(10, 100))