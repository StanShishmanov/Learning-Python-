def read_matrix(cells_delimiter):
    n = int(input())
    return [list(map(int, input().split(cells_delimiter))) for _ in range(n)]

def calculate_primary_diagonal_sum(matrix):
    the_sum = 0
    n = len(matrix)
    for x in range(n):
        the_sum += matrix[x][x]
    return the_sum

def calculate_secondary_diagonal_sum(matrix):
    the_sum = 0
    n = len(matrix)
    for x in range(n):
        the_sum += matrix[x][n - x - 1]
    return the_sum

def calculate_sums(matrix, primary_func, secondary_func):
    return abs(primary_func(matrix) - secondary_func(matrix)) 


matrix = read_matrix(' ')
print(abs(calculate_primary_diagonal_sum(matrix) - calculate_secondary_diagonal_sum(matrix)))