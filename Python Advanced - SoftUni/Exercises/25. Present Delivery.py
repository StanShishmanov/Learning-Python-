count_of_presents = int(input())
n = int(input())
nice_kids = 0
happy_nice_kids = 0
matrix = []
current_santa_position = (0, 0)
for _ in range(n):
    matrix.append(list(input().split()))

while True:
    if not count_of_presents:
        break
    else:
        command = input()
        
        if command == "Christmas morning":
            break
        else:
            nice_kids = 0
            for row in range(len(matrix)):
                for col in range(len(matrix[0])):
                    if matrix[row][col] == 'S':
                        current_santa_position = (row, col)
                    elif matrix[row][col] == 'V':
                        nice_kids += 1
            if command == 'up':
                next_position = (current_santa_position[0] - 1, current_santa_position[1])
                
            elif command == 'down':
                next_position = (current_santa_position[0] + 1, current_santa_position[1])


            elif command == 'left':
                next_position = (current_santa_position[0], current_santa_position[1] - 1)
            elif command == 'right':
                next_position = (current_santa_position[0], current_santa_position[1] + 1)

            if matrix[next_position[0]][next_position[1]] != '-':
                if matrix[next_position[0]][next_position[1]] == 'V':
                    count_of_presents -= 1
                    nice_kids -= 1
                    happy_nice_kids += 1
                    matrix[current_santa_position[0]][current_santa_position[1]] = '-'
                    matrix[next_position[0]][next_position[1]] = 'S'
                    current_santa_position = next_position

                elif matrix[next_position[0]][next_position[1]] == 'X':
                    matrix[current_santa_position[0]][current_santa_position[1]] = '-'
                    matrix[next_position[0]][next_position[1]] = 'S'
                    current_santa_position = next_position
                    

                elif matrix[next_position[0]][next_position[1]] == 'C':
                    matrix[current_santa_position[0]][current_santa_position[1]] = '-'
                    matrix[next_position[0]][next_position[1]] = 'S'

                    if matrix[next_position[0] - 1][next_position[1]] == 'V' or matrix[next_position[0] - 1][next_position[1]] == 'X':
                        count_of_presents -= 1
                        if matrix[next_position[0] - 1][next_position[1]] == 'V':
                            nice_kids -= 1
                            happy_nice_kids += 1
                        matrix[next_position[0] - 1][next_position[1]] = '-'
                    
                    if matrix[next_position[0] + 1][next_position[1]] == 'V' or matrix[next_position[0] + 1][next_position[1]] == 'X':
                        count_of_presents -= 1
                        if matrix[next_position[0] + 1][next_position[1]] == 'V':
                            nice_kids -= 1
                            happy_nice_kids += 1
                        matrix[next_position[0] + 1][next_position[1]] = '-'
                    
                    if matrix[next_position[0]][next_position[1] + 1] == 'V' or matrix[next_position[0]][next_position[1] + 1] == 'X':
                        count_of_presents -= 1
                        if matrix[next_position[0]][next_position[1] + 1] == 'V':
                            nice_kids -= 1
                            happy_nice_kids += 1
                        matrix[next_position[0]][next_position[1] + 1] = '-'

                    if matrix[next_position[0]][next_position[1] - 1] == 'V' or matrix[next_position[0]][next_position[1] - 1] == 'X':
                        count_of_presents -= 1
                        if matrix[next_position[0]][next_position[1] - 1] == 'V':
                            nice_kids -= 1
                            happy_nice_kids += 1
                        matrix[next_position[0]][next_position[1] - 1] = '-'
            else:
                matrix[current_santa_position[0]][current_santa_position[1]] = '-'
                matrix[next_position[0]][next_position[1]] = 'S'
                current_santa_position = next_position

if count_of_presents <= 0 and nice_kids > 0:
    print('Santa ran out of presents!')

[print(' '.join(row)) for row in matrix]
if count_of_presents >= 0 and nice_kids == 0:
    print(f"Good job, Santa! {happy_nice_kids} happy nice kid/s.")
else:
    print(f'No presents for {nice_kids} nice kid/s.')