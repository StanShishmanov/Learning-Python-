from collections import deque

commands = input().split()
numbers = input().split()

to_pop = int(commands[1])
to_look_for = int(commands[2])


my_queue = deque()
for num in numbers:
    my_queue.append(int(num))
i = 0
while i < to_pop:
    my_queue.popleft()
    i += 1
if to_look_for in my_queue:
    print('True')
else:
    if my_queue:
        print(min(my_queue))
    else:
        print(0)