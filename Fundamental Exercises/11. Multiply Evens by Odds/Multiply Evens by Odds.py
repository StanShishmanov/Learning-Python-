def multiplier(number):
    even_sum = 0
    odd_sum = 0
    while number != 0:
        digit = number % 10
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
        number //= 10
    return even_sum * odd_sum

input_number = abs(int(input()))

print(multiplier(input_number))