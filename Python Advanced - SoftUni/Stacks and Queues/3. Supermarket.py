from collections import deque
def solve():
    
    customers = deque()
    while True:
        my_input = input()

        if my_input == 'End':
            print(f'{len(customers)} people remaining.')
            break

        else:
            if my_input == 'Paid':
                while customers:
                    print(customers.popleft())
                
            else:
                customers.append(my_input)

solve()