green_light_duration = int(input())
free_window_duration = int(input())
crash_happened = False
cars = []
cars_passed = []

while not crash_happened:
    command = input()
    if command == 'END':
        break
    else:
        if command != 'green':
            cars.append(command)

        else:
            green_light = green_light_duration
            free_window = free_window_duration
            i = 0
            for i in range(len(cars)):
                i += 1
                if cars and (green_light >= len(cars[0])):
                    green_light -= len(cars[0])
                    cars_passed.append(cars.pop(0))
                elif cars and (green_light < len(cars[0])):
                    time_remaining = green_light + free_window
                    if green_light <= 0:
                        continue
                    elif time_remaining > 0 and (time_remaining >= len(cars[0])):
                        car = cars[0]
                        time_remaining -= len(car)
                        cars_passed.append(cars.pop(0))
                        green_light = 0
                        free_window = 0
                    elif time_remaining > 0 and time_remaining < len(cars[0]):
                        car = cars[0]

                        print('A crash happened!')
                        car_hit = time_remaining
                        print(f'{car} was hit at {car[time_remaining]}.')
                        crash_happened = True
                        break
if not crash_happened:
    print('Everyone is safe.')
    print(f'{len(cars_passed)} total cars passed the crossroads.')