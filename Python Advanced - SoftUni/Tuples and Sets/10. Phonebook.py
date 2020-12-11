people = {}
searching = False

while not searching:
    command = input()
    
    if command == 'search':
        searching = True
        break
    name = command.split('-')[0]
    phone = command.split('-')[1]
    if name in people.keys():
        people[name] = phone
    else:
        people[name] = phone

while searching: 
    command = input()
    if command == 'stop':
        break
    else:
        
        if command in people.keys():
            print(f'{command} -> {people[command]}')
        else:
            print(f'Contact {command} does not exist.')