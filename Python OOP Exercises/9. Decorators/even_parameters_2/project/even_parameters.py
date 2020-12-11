def even_parameters(func):
    def wrapper(*args):
        nums = []
        for num in args:
            if isinstance(num, int):
                if num % 2 == 0:
                    nums.append(num)
                else:
                    return "Please use only even numbers!"
            else:
                return "Please use only even numbers!"

        if len(nums) == len(args):
            result = func(*args)
            return result
    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))

@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
