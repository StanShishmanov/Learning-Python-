from collections import deque
def solve():
    total_petrol_pumps = int(input())
    pumps = []

    for i in range(total_petrol_pumps):
        pair = [int(num) for num in input().split()]
        pumps.append(pair[0] - pair[1])
    
    current = 0;
    position = 0;

    for i in range(total_petrol_pumps):
        current += pumps[i];
        if (current < 0):

            current = 0
            position = i + 1
    print(position)

solve()