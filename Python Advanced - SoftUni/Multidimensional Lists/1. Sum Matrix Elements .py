def read_matrix(cells_delimiter):
    (rows_count, columns_count) = map(int, input().split(cells_delimiter))
    return [list(map(int, input().split(cells_delimiter))) for _ in range(rows_count)]

def sum_matrix(matrix):
    the_sum = 0
    rows_count = len(matrix)
    columns_count = len(matrix[0])

    for row_index in range(rows_count):
        the_sum += sum(matrix[row_index])
    return the_sum

matrix = read_matrix(' ')
print(sum_matrix(matrix))
print(matrix)