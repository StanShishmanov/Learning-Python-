n = int(input())
matrix = [[int(num) for num in input().split(', ')] for num in range(n)]

primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal_first = [matrix[i][j] for i in range(n) for j in range(n) if i + j == n -1]
secondary_diagonal = [matrix[i][n - i - 1] for i in range(n)]

print('First diagonal: ' + ', '.join(map(str, primary_diagonal)) + '. Sum: ' + str(sum(primary_diagonal)))
print('Second diagonal: ' + ', '.join(map(str, secondary_diagonal)) + '. Sum: ' + str(sum(secondary_diagonal)))