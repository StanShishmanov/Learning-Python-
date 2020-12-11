(rows, columns) = [int(x) for x in (input().split())]
matrix = []
player_won = False
player_died = False
player_killed = False
for row in range(rows):
    matrix.append([x for x in input()])

player_moves = [x for x in input()]

player_start_position = []

for row in range(rows):
    for column in range(columns):
        player = matrix[row][column]
        if player == 'P':
            player_start_position = [row, column]

def bunny_spread(rows, columns, matrix):
    dot_positions = []
    global player_killed
    for row in range(rows):
        for column in range(columns):
            char = matrix[row][column]
            if char == 'B':

                # To the left
                if column > 0: 
                    if matrix[row][column - 1] == '.':
                        dot_positions.append([row, column - 1])
                    elif matrix[row][column - 1] == 'P':
                        dot_positions.append([row, column - 1])
                        player_killed = True

                # To the right
                if columns > column + 1:
                    if matrix[row][column + 1] == '.':
                        dot_positions.append([row, column + 1])
                    elif matrix[row][column + 1] == 'P':
                        dot_positions.append([row, column + 1])
                        player_killed = True

                # Going up
                if row > 0:
                    if matrix[row - 1][column] == '.':
                        dot_positions.append([row - 1, column])
                    elif matrix[row - 1][column] == 'P':
                        dot_positions.append([row - 1, column])
                        player_killed = True

                # Going down
                if rows > row + 1:
                    if matrix[row + 1][column] == '.':
                        dot_positions.append([row + 1, column])
                    elif matrix[row + 1][column] == 'P':
                        dot_positions.append([row + 1, column])
                        player_killed = True

    dot_columns = len(dot_positions[0])
    dot_rows = len(dot_positions)

    for row in range(dot_rows):
        for column in range(dot_columns):
            next_position = dot_positions[row]
            matrix[next_position[0]][next_position[1]] = 'B'

    dot_positions = []
    
while True:
    if player_won:
        break
    elif player_died or player_killed:
        break
    else:
        for step in player_moves:
            if player_won:
                break
            elif player_died:
                break
            else:
                if step == 'U':
                    for row in range(rows):
                        for column in range(columns):
                            if row == player_start_position[0] and column== player_start_position[1]:
                                matrix[player_start_position[0]][player_start_position[1]] = '.'
                                if row > 0:
                                    next_position = [row - 1, column]
                                    if matrix[next_position[0]][next_position[1]] == 'B':
                                        player_died = True
                                        player_start_position = next_position
                                        bunny_spread(rows, columns, matrix)
                                        break
                                    else:
                                        player_start_position = next_position
                                        matrix[next_position[0]][next_position[1]] = 'P'
                                        bunny_spread(rows, columns, matrix)
                                else:
                                    player_won = True
                                    player_start_position = next_position
                                    bunny_spread(rows, columns, matrix)

                elif step == 'D':
                    for row in range(rows):
                        for column in range(columns):
                            if row == player_start_position[0] and column== player_start_position[1]:
                                matrix[player_start_position[0]][player_start_position[1]] = '.'
                                if row < rows:
                                    next_position = [row + 1, column]
                                    if matrix[next_position[0]][next_position[1]] == 'B':
                                        player_died = True
                                        player_start_position = next_position
                                        bunny_spread(rows, columns, matrix)
                                        break
                                    else:
                                        player_start_position = next_position
                                        matrix[next_position[0]][next_position[1]] = 'P'
                                        bunny_spread(rows, columns, matrix)
                                else:
                                    player_won = True
                                    player_start_position = next_position
                                    bunny_spread(rows, columns, matrix)

                elif step == 'L':
                    for row in range(rows):
                        for column in range(columns):
                            if row == player_start_position[0] and column== player_start_position[1]:
                                matrix[player_start_position[0]][player_start_position[1]] = '.'
                                if column > 0:
                                    next_position = [row, column - 1]
                                    if matrix[next_position[0]][next_position[1]] == 'B':
                                        player_died = True
                                        player_start_position = next_position
                                        bunny_spread(rows, columns, matrix)
                                        break
                                    else:
                                        player_start_position = next_position
                                        matrix[next_position[0]][next_position[1]] = 'P'
                                        bunny_spread(rows, columns, matrix)
                                else:
                                    player_won = True
                                    player_start_position = next_position
                                    bunny_spread(rows, columns, matrix)
                            

                elif step == 'R':
                    for row in range(rows):
                        for column in range(columns):
                            if row == player_start_position[0] and column== player_start_position[1]:
                                matrix[player_start_position[0]][player_start_position[1]] = '.'
                                if column > 0:
                                    next_position = [row, column + 1]
                                    if matrix[next_position[0]][next_position[1]] == 'B':
                                        player_died = True
                                        player_start_position = next_position
                                        bunny_spread(rows, columns, matrix)
                                        break
                                    else:
                                        player_start_position = next_position
                                        matrix[next_position[0]][next_position[1]] = 'P'
                                        bunny_spread(rows, columns, matrix)
                                else:
                                    player_won = True
                                    player_start_position = next_position
                                    bunny_spread(rows, columns, matrix)

[print(''.join(row)) for row in matrix]
if player_won:
    print(f'won: {player_start_position[0]} {player_start_position[1]}')
if player_died:
    print(f'dead: {player_start_position[0]} {player_start_position[1]}')