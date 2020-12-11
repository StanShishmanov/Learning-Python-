from collections import deque

bullet_price = int(input())
barrel_capacity = int(input())
bullet_sizes = deque([int(x) for x in input().split()])
lock_sizes = deque([int(x) for x in input().split()])
money = int(input())
total_bullets = 0
while True:
    if not lock_sizes:
        print(f'{total_bullets} bullets left. Earned ${money}')
        break
    elif not bullet_sizes:
        print(f"Couldn't get through. Locks left: {len(lock_sizes)}")
        break
    else:
        total_bullets = barrel_capacity

        for i in range(barrel_capacity):
            total_bullets -= 1
            bullet = bullet_sizes.pop()
            lock = lock_sizes.popleft()
            if lock >= bullet:
                print('Bang!')
                
            else:
                lock_sizes.appendleft(lock)
                print('Ping!')
            money -= bullet_price
        if bullet_sizes:
            print('Reloading!')
            total_bullets = barrel_capacity