from collections import deque
quantity = int(input())
biggest_order = 0
orders = deque([int(x) for x in input().split()])

for i in orders:
    if i > biggest_order:
        biggest_order = i
print(biggest_order)

while orders:
    order = orders.popleft()
    if (quantity - order) < 0:
        orders.append(order)
        
        print(f'Orders left: ' + ' '.join(map(str, orders)))
        break
    else:
        quantity -= order
if not orders:
    print("Orders complete")