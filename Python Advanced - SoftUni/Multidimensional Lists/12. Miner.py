rows_count = int(input())
matrix = []
steps = [x for x in input().split()]
start_position = [0, 0]
next_position = [0, 0]
end_game = False
coals = 0
coal_available = 0

for _ in range(rows_count):
    matrix.append(input().split())

# Find start position
for row in range(rows_count):
    for col in range(rows_count):
        start = matrix[row][col]
        if start == 's':
            start_position = [row, col]

for row in range(rows_count):
    for col in range(rows_count):
        coal = matrix[row][col]
        if coal == 'c':
            coal_available += 1
# Move player
if not end_game:
    for i in steps:
        if i == 'up':
            for row in range(rows_count):
                for col in range(rows_count):
                    if row == start_position[0] and col == start_position[1]:
                        if row > 0:
                            next_position = [row - 1, col]
                            if matrix[next_position[0]][next_position[1]] == 'c':
                                matrix[next_position[0]][next_position[1]] = '*'
                                coals += 1
                            if matrix[next_position[0]][next_position[1]] == 'e':
                                end_game = True
            start_position = next_position
                
        elif i == 'down':
            for row in range(rows_count):
                for col in range(rows_count):
                    if row == start_position[0] and col == start_position[1]:
                        if row + 1 < len(matrix):
                            next_position = [row + 1, col]
                            if matrix[next_position[0]][next_position[1]] == 'c':
                                matrix[next_position[0]][next_position[1]] = '*'
                                coals += 1
                            if matrix[next_position[0]][next_position[1]] == 'e':
                                end_game = True
            start_position = next_position

        elif i == 'left':
            for row in range(rows_count):
                for col in range(rows_count):
                    if row == start_position[0] and col == start_position[1]:
                        if col > 0:
                            next_position = [row,col - 1]
                            if matrix[next_position[0]][next_position[1]] == 'c':
                                matrix[next_position[0]][next_position[1]] = '*'
                                coals += 1
                            if matrix[next_position[0]][next_position[1]] == 'e':
                                end_game = True
            start_position = next_position

        elif i == 'right':
            for row in range(rows_count):
                for col in range(rows_count):
                    if row == start_position[0] and col == start_position[1]:
                        if col + 1 < len(matrix):
                            next_position = [row,col + 1]
                            if matrix[next_position[0]][next_position[1]] == 'c':
                                matrix[next_position[0]][next_position[1]] = '*'
                                coals += 1
                            if matrix[next_position[0]][next_position[1]] == 'e':
                                end_game = True
            start_position = next_position

if end_game:
    print(f'Game over! {tuple(start_position)}')

elif coals == coal_available:
    print(f'You collected all coals! {tuple(start_position)}')
else:
    print(f'{coal_available - coals} coals left. {tuple(start_position)}')