def read_input():
    n = int(input())
    return (
        [input() for _ in range(n)],
        input()
    )

def find_position(matrix, symbol):
    n = len(matrix)
    for r in range(n):
        for c in range(n):
            if matrix[r][c] == symbol:
                return (r, c)
    return None

(matrix, symbol) = read_input()

result = find_position(matrix, symbol)
if result:
    (row, col) = result
    print(f'({row}, {col})')
else:
    print(f'{symbol} does not occur in the matrix')