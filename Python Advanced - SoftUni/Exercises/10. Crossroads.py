from collections import deque

green_duration = int(input())
free_window = int(input())
crashed = False
cars = deque()
cars_passed = 0

while not crashed:
    command = input()
    if command == 'END':
        break
    else:
        if command != 'green':
            cars.append(command)
        else:
            green_light = green_duration
            window_time = free_window
            if cars:
                for i in range(len(cars)):
                    if green_light > 0:
                        car = cars.popleft()
                        if (green_light + window_time) - len(car) >= 0:
                            if green_light - len(car) <= 0:
                                window_time = (green_light + window_time) - len(car) 
                                green_light = 0
                                cars_passed += 1
                            else:
                                green_light -= len(car)
                                cars_passed += 1
                        else:
                            hit = len(car) - (green_light + window_time)
                            crashed = True
                            print('A crash happened!')
                            print(f'{car} was hit at {car[-hit]}.')
                            break

if not crashed:
    print('Everyone is safe.')
    print(f'{cars_passed} total cars passed the crossroads.')