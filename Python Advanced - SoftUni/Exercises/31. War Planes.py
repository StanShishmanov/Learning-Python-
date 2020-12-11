n = int(input())
matrix = []

for i in range(n):
    matrix.append(list(input().split()))

m = int(input())
commands = []

for i in range(m):
    commands.append(list(input().split()))

starting_position = (0, 0)

def find_plane(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == 'p':
                starting_position = (row, col)
    return starting_position


def find_targets(matrix):
    total_targets = 0
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == 't':
                total_targets += 1
    return total_targets

total_targets = find_targets(matrix)
initial_targets = total_targets
all_tagets_destroyed = False


for comm in range(len(commands)):
    command = commands[comm]
    action = command[0]
    direction = command[1]
    steps = int(command[2])
    starting_position = find_plane(matrix)
    if action == 'move':
        if direction == 'down':
            try:
                future_direction = (starting_position[0] + steps, starting_position[1])
                
                if matrix[future_direction[0]][future_direction[1]] == '.':
                    matrix[starting_position[0]][starting_position[1]] = '.'
                    starting_position = (future_direction[0], future_direction[1])
                    matrix[future_direction[0]][future_direction[1]] = 'p'
            except IndexError:
                continue

        elif direction == 'up':
            try:
                future_direction = (starting_position[0] - steps, starting_position[1])
                if matrix[future_direction[0]][future_direction[1]] == '.':
                    matrix[starting_position[0]][starting_position[1]] = '.'
                    starting_position = (future_direction[0], future_direction[1])
                    matrix[future_direction[0]][future_direction[1]] = 'p'

            except IndexError:
                continue

        elif direction == 'right':
            try:
                future_direction = (starting_position[0], starting_position[1] + steps)
                if matrix[future_direction[0]][future_direction[1]] == '.':
                    matrix[starting_position[0]][starting_position[1]] = '.'
                    starting_position = (future_direction[0], future_direction[1])
                    matrix[future_direction[0]][future_direction[1]] = 'p'
            except IndexError:
                continue

        elif direction == 'left':
            try:
                future_direction = (starting_position[0], starting_position[1] - steps)
                if matrix[future_direction[0]][future_direction[1]] == '.':
                    matrix[starting_position[0]][starting_position[1]] = '.'
                    starting_position = (future_direction[0], future_direction[1])
                    matrix[future_direction[0]][future_direction[1]] = 'p'
            except IndexError:
                continue

    # SHOOTING
    elif action == 'shoot':
        if direction == 'down':
            try:
                future_direction = (starting_position[0] + steps, starting_position[1])
                if matrix[future_direction[0]][future_direction[1]] == '.':
                    matrix[future_direction[0]][future_direction[1]] = 'x'
                elif matrix[future_direction[0]][future_direction[1]] == 't':
                    matrix[future_direction[0]][future_direction[1]] = 'x'
                    total_targets -= 1
                    if total_targets == 0:
                        all_tagets_destroyed = True
                        break
            except IndexError:
                continue

        elif direction == 'up':
            try:
                future_direction = (starting_position[0] - steps, starting_position[1])
                if matrix[future_direction[0]][future_direction[1]] == '.':
                    matrix[future_direction[0]][future_direction[1]] = 'x'
                elif matrix[future_direction[0]][future_direction[1]] == 't':
                    matrix[future_direction[0]][future_direction[1]] = 'x'
                    total_targets -= 1
                    if total_targets == 0:
                        all_tagets_destroyed = True
                        break
            except IndexError:
                continue

        elif direction == 'right':
            try:
                future_direction = (starting_position[0], starting_position[1] + steps)
                if matrix[future_direction[0]][future_direction[1]] == '.':
                    matrix[future_direction[0]][future_direction[1]] = 'x'
                elif matrix[future_direction[0]][future_direction[1]] == 't':
                    matrix[future_direction[0]][future_direction[1]] = 'x'
                    total_targets -= 1
                    if total_targets == 0:
                        all_tagets_destroyed = True
                        break
            except IndexError:
                continue

        elif direction == 'left':
            try:
                future_direction = (starting_position[0], starting_position[1] - steps)
                if matrix[future_direction[0]][future_direction[1]] == '.':
                    matrix[future_direction[0]][future_direction[1]] = 'x'
                elif matrix[future_direction[0]][future_direction[1]] == 't':
                    matrix[future_direction[0]][future_direction[1]] = 'x'
                    total_targets -= 1
                    if total_targets == 0:
                        all_tagets_destroyed = True
                        break
            except IndexError:
                continue
if all_tagets_destroyed:
    print(f"Mission accomplished! All {initial_targets} targets destroyed.")
else:
    print(f"Mission failed! {total_targets} targets left.")
[print(' '.join(row)) for row in matrix]