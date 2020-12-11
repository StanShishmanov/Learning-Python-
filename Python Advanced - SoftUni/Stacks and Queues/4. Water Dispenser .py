from collections import deque

def solve():

    total_water = int(input())
    people = deque()

    while True:
        command = input()
        
        if command == 'Start':
            break
        people.append(command)
        
    while people:
        
        liters_asked = input()
        if liters_asked == "End":
            break
        if liters_asked.startswith("refill"):
            total_water += int(liters_asked.split()[1])
        else:    
            current_name = people.popleft()
            if int(liters_asked) > total_water:
                print(f'{current_name} must wait')
                people.append(current_name)

            else:
                print(f'{current_name} got water')
                total_water -= int(liters_asked)
    print(f'{total_water} liters left')
solve()