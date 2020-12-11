initial_str = input()
n = int(input())
matrix = []
dirs = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}
for row in range(n):
    line = list(input())
    if "P" in line:
        player_position = [row, line.index("P")]
    matrix.append(line)

m = int(input())
moves = []
for _ in range(m):
    move = input()
    direction_change = dirs[move]
    next_row = player_position[0] + direction_change[0]
    next_col = player_position[1] + direction_change[1]
    next_pos = [next_row, next_col]

    if 0 <= next_row < n and 0 <= next_col < n:
        if matrix[next_row][next_col] == '-':
            matrix[player_position[0]][player_position[1]] = '-'
            player_position = next_pos
            matrix[player_position[0]][player_position[1]] = 'P'

        else:
            matrix[player_position[0]][player_position[1]] = '-'
            initial_str += matrix[next_row][next_col]
            player_position = next_pos
            matrix[player_position[0]][player_position[1]] = 'P'
    else:
        initial_str = initial_str[:-1]
print(initial_str)
[print(''.join(row)) for row in matrix]