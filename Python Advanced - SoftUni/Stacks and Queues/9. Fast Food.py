from collections import deque

def solve():
    total_food = int(input())
    sequence = input().split()
    sequence = [int(num) for num in sequence]
    my_deque = deque(sequence)
    
    total_orders = 0
    print(max(my_deque))
    complete = True
    while my_deque:
        order = my_deque[0]
        total_orders += order

        if total_orders <= total_food:
            my_deque.popleft()
        else:
            my_list = list(my_deque)
            print('Orders left: ' + ' '.join([str(i) for i in my_list]))
            complete = False
            break
    if complete:
        print('Orders complete')
              
solve()