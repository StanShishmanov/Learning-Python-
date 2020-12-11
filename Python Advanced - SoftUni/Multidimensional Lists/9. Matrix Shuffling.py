def read_matrix():
    (rows_count, columns_count) = map(int, input().split())
    return [input().split() for _ in range(rows_count)]

def check_input(command, matrix):
    is_swap_correct = command.split()[0]
    coordinates = list(map(int, command.split()[1:]))
    rows_length = len(matrix)
    columns_length = len(matrix[0])
    invalid = False
    
    if (is_swap_correct == 'swap' and len(command.split()) == 5):
        
        row_one = coordinates[0]
        col_one = coordinates[1]
        row_two = coordinates[2]
        col_two = coordinates[3]

        if (row_one >= 0 and row_one < rows_length) and \
            (col_one >= 0 and col_one < columns_length) and \
            (row_two >= 0 and row_two < rows_length) and \
                (col_two >= 0 and col_two < columns_length):
                return coordinates, True
        else:
            return False

def coordinate_swapper(command, matrix):
    if check_input(command, matrix):
        coordinates = list(map(int, command.split()[1:]))
        row_one = coordinates[0]
        col_one = coordinates[1]
        row_two = coordinates[2]
        col_two = coordinates[3]

        matrix[row_one][col_one], matrix[row_two][col_two] = matrix[row_two][col_two], matrix[row_one][col_one]
        [print(' '.join(map(str, row))) for row in matrix]
        
    else:
        print('Invalid input!')
matrix = read_matrix()

while True:
    command = input()
    if command == 'END':
        break
    else:
        coordinate_swapper(command, matrix)