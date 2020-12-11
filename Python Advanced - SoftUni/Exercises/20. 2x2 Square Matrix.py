def read_matrix(cells_delimiter):
    line = input().split()
    return [list(input().split(cells_delimiter)) for _ in range(int(line[0]))]


def find_squares(matrix):
    total_matches = 0
    n = len(matrix)
    m = len(matrix[0])
    for row in range(n - 1):
        for column in range(m - 1):
            if matrix[row][column] == matrix[row][column + 1] == matrix[row + 1][column] == matrix[row + 1][column + 1]:
                total_matches += 1

    return total_matches


matrix = read_matrix(' ')
print(find_squares(matrix))
"""
3 4
A B B D
E B B B
I J B B

"""