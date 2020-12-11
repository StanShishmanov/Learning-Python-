cars = set()
while True:
    command = input()
    if command == 'END':
        break
    else:
        action = command.split(', ')[0]
        number = command.split(', ')[1]
        if action == 'IN':
            
            if number not in cars:
                cars.add(number)
        else:
            if number in cars:
                cars.discard(number)
if cars:
    for car in cars:
        print(car)
else:
    print('Parking Lot is Empty')