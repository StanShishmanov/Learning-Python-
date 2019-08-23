my_input = [float(i) for i in (input().split(' '))]
index = 1
while index != len(my_input):
    previous = my_input[index - 1]
    current = my_input[index]
    if previous == current:
        my_input[index] = previous + current
        my_input.remove(my_input[index - 1])
        index = 0
    index += 1
print(f' '.join(map(str, my_input)))