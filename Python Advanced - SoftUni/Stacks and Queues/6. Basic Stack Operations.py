commands = input().split()
numbers = input().split()
my_stack = [int(num) for num in numbers]
to_pop = int(commands[1])
to_look_for = int(commands[2])

i = 0
while i < to_pop:
    i += 1
    my_stack.pop()

if to_look_for in my_stack:
    print('True')
else:
    if my_stack:
        print(min(my_stack))
    else:
        print(0)