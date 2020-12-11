from collections import deque

def solve(children, number):
    
    circle = deque(children)
    index = 0
    while circle:
        index += 1
        child = circle.popleft()
        if index == number:
            index = 0
            if circle:
                print(f'Removed {child}')
            else:
                print(f'Last is {child}')
        else:
            circle.append(child)
    
solve(input().split(), int(input()))