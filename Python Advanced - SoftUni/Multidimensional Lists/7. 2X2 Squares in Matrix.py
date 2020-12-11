def read_matrix(cells_delimiter):
    (rows_count, columns_count) = map(int, input().split(' '))
    return [list(input().split(cells_delimiter)) for _ in range(rows_count)]

def find_matches(matrix):
    rows_count = len(matrix)
    columns_count = len(matrix[0])
    matches_found = 0
    for row in range(rows_count - 1):
        for col in range(columns_count - 1):
            if matrix[row][col] == \
            matrix[row][col + 1] == \
            matrix[row + 1][col] == \
            matrix[row + 1][col + 1]:
                matches_found += 1
    return matches_found

matrix = read_matrix(' ')
print(find_matches(matrix))