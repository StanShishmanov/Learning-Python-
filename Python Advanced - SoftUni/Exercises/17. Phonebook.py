people = {}

while True:
    command = input()
    if command != 'search':
        name = command.split('-')[0]
        number = command.split('-')[1]
        people[name] = number
    else:
        break

while True:
    command = input()
    if command != 'stop':
        
        if command in people:
            print(f"{command} -> {people[command]}")
        else:
            print(f'Contact {command} does not exist.')
    else:
        break