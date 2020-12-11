# Remove from each shot
bullet_price = int(input())

# Reload after it is out
barrel_size = int(input())

# Used to unclock if == < than the lock size
bullet_sizes = input().split()
bullet_sizes = [int(bullet) for bullet in bullet_sizes[::-1] if bullet]

# Must be == or > than the bullet size
locks = [int(lock) for lock in input().split()]

# Remove from after each shot
prize_money = int(input())
shots = 0

out_of_bullets = False
out_of_locks = False
all_is_out = False

while True:
    
    if not bullet_sizes and not locks:
        all_is_out = True
        break
    if not bullet_sizes:
        out_of_bullets = True
    
        break
    if shots == barrel_size:
        print('Reloading!')
        shots = 0
        continue
    if not locks:
        out_of_locks = True
        
        break
    else:
        bullet = bullet_sizes.pop(0)
        lock = locks[0]
        shots += 1
        prize_money -= bullet_price

        if bullet <= lock:
            locks.pop(0)
            print('Bang!')
        else:
            print('Ping!')

if all_is_out:
    print(f'{len(bullet_sizes)} bullets left. Earned ${prize_money}')
elif out_of_bullets:
    print(f"Couldn't get through. Locks left: {len(locks)}")
elif out_of_locks:
    print(f'{len(bullet_sizes)} bullets left. Earned ${prize_money}')