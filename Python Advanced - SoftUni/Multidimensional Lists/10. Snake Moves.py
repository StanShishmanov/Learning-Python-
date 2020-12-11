from collections import deque
rows_count, cols_count = [int(x) for x in input().split()]
snake = deque(input())

matrix = []

for _ in range(rows_count):
    matrix.append(["" for _ in range(cols_count)])

for row in range(rows_count):
    if row % 2 == 0:
        for column in range(cols_count):
            element = snake.popleft()
            matrix[row][column] = element
            snake.append(element)
    else:
        for column in range(cols_count - 1, -1, -1):
            element = snake.popleft()
            matrix[row][column] = element
            snake.append(element)

[print("".join(row)) for row in matrix]