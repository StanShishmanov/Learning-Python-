def read_matrix(cells_delimiter):
    n = int(input())
    return [list(map(int, input().split(cells_delimiter))) for _ in range(n)]
    

def calculate_primary_diagonal(matrix):
    diag_sum = 0
    n = len(matrix)
    for x in range(n):
        diag_sum += matrix[x][x]
    return diag_sum


def calculate_secondary_diagonal(matrix):
    diag_sum = 0
    n = len(matrix)
    for x in range(n):
        diag_sum += matrix[x][n - x - 1]
    return diag_sum


def absolute_sum(matrix, calculate_primary_diagonal, calculate_secondary_diagonal):
    return abs(calculate_primary_diagonal(matrix) - calculate_secondary_diagonal(matrix))


matrix = read_matrix(' ')
print(absolute_sum(matrix, calculate_primary_diagonal, calculate_secondary_diagonal))


# To iterate over a matrix I need the lenght and indexing