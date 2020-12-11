def read_matrix():
    (rows, columns) = input().split()
    return [input().split() for _ in range(int(rows))]

matrix = read_matrix()

while True:
    command = input()
    coordinates = []
    invalid_input = False
    if command == 'END':
        break
    else:
        coordinates = [int(x) for x in command.split()[1:]]
        if command.split()[0] != 'swap' or len(coordinates) != 4:
            print('Invalid input!')
            
            continue

        else:
            for coor in coordinates:
                if coor > len(matrix) or coor < 0:
                    print('Invalid input!')
                    invalid_input = True
                    break
    if not invalid_input:
        row_one = int(coordinates[0])
        col_one = int(coordinates[1])
        row_two = int(coordinates[2])
        col_two = int(coordinates[3])
        new_matrix = matrix[row_one][col_one]
        matrix[row_one][col_one] = matrix[row_two][col_two]
        matrix[row_two][col_two] = new_matrix
        [print(' '.join(map(str, row))) for row in matrix]