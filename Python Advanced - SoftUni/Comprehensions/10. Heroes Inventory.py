inventory = {name: {} for name in input().split(', ')}

while True:
    command = input()
    if command == 'End':
        break
    else:
        name, item, cost = command.split('-')
        if name not in inventory:
            inventory[name] = {}
            if item not in inventory[name]:
                inventory[name][item] = int(cost)
        else:
            if item not in inventory[name]:
                inventory[name][item] = int(cost)

[print(f'{key} -> Items: {len(inventory[key])}, Cost: {sum(inventory[key].values())}') for key in inventory]