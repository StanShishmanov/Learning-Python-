from collections import deque
cups = deque([int(x) for x in input().split()])
bottles = deque([int(x) for x in input().split()])
wasted_water = 0
no_cups_left = False
no_bottles_left = False 


while True:
    if not cups:
        no_cups_left = True
        break
    elif not bottles:
        no_bottles_left = True
        break
    else:
        cup = cups.popleft()
        bottle = bottles.pop()
        if cup == bottle:
            continue
        else:
            if cup > bottle:
                cup -= bottle
                cups.appendleft(cup)
            else:
                wasted_water += bottle - cup

if no_cups_left:
    print(f'Bottles: ' + ' '.join(map(str, bottles)))
    print(f"Wasted litters of water: {wasted_water}")
elif no_bottles_left:
    print(f'Cups: ' + ' '.join(map(str, cups)))
    print(f"Wasted litters of water: {wasted_water}")