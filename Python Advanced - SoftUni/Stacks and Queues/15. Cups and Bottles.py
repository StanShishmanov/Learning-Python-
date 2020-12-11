cups = input().split()
cups = [int(cup) for cup in cups]
water_bottles = input().split()
water_bottles = [int(water) for water in water_bottles[::-1]]

wasted_water = 0

no_cups = False
no_water_bottles = False
everything_is_out = False

while True:
    if not cups and not water_bottles:
        everything_is_out = True
        break
    
    if not cups:
        no_cups = True
        break
    if not water_bottles:
        no_water_bottles = True
        break

    else:
        cup = cups.pop(0)
        bottle = water_bottles.pop(0)
        if bottle == cup:
            continue
        else:
            if bottle > cup:
                wasted_water += (bottle - cup)
            else:
                cup -= bottle
                cups.insert(0, cup)

if no_cups:
    print('Bottles: ' + ' '.join(map(str, water_bottles)))
    print(f'Wasted litters of water: {wasted_water}')
if no_water_bottles:
    print('Cups: ' + ' '.join(map(str, cups)))
    print(f'Wasted litters of water: {wasted_water}')