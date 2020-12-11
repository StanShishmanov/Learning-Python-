from collections import deque
(rows, cols) = [int(x) for x in input().split()]

matrix = []
for _ in range(rows):
    matrix.append(["" for _ in range(cols)])

snake = deque(input())

for row in range(rows):
    if row % 2 == 0:
        for col in range(cols):
            element = snake.popleft()
            matrix[row][col] = element
            snake.append(element)
        
    else:
        for col in range(cols - 1, -1, -1):
            element = snake.popleft()
            matrix[row][col] = element
            snake.append(element)

[print("".join(row)) for row in matrix]