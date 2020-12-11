def read_matrix():
    (rows_count, columns_count) = map(int, input().split())
    return [list(map(int, input().split())) for _ in range(rows_count)]


def find_best_submatrix(matrix):
    rows_count = len(matrix)
    columns_count = len(matrix[0])
    best_sum = None
    best_start = None

    for row in range(rows_count - 2):
        for col in range(columns_count - 2):
            current_sum = matrix[row][col] + \
            matrix[row][col + 1] + \
            matrix[row][col + 2] + \
            matrix[row + 1][col] + \
            matrix[row + 1][col + 1] + \
            matrix[row + 1][col + 2] + \
            matrix[row + 2][col] + \
            matrix[row + 2][col + 1] + \
            matrix[row + 2][col + 2]
        
            if best_sum:
                if best_sum < current_sum:

                    best_sum = current_sum
                    best_start = (row, col)
            else:
                best_sum = current_sum
                best_start = (row, col)

    (row, col) = best_start

    best_submatrix = [
        [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
        [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
        [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]],
    ]

    return (best_sum, best_submatrix)

matrix = read_matrix()

(best_sum , find_best_submatrix) = find_best_submatrix(matrix)
print(f'Sum = {best_sum}')
[print(' '.join(map(str, row))) for row in find_best_submatrix]