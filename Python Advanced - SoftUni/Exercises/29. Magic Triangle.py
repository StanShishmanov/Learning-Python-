def get_magic_triangle(n):
    matrix = []
    num = 1
    for i in range(n):
        my_list = [1]
        for j in range(i):
            my_list.append(num)
        matrix.append(my_list)

    for row in range(len(matrix)):
        if row >= 2:
            previous_row = matrix[row - 1]
            current_row = matrix[row]
            counter = 1
            for num in range(len(previous_row) - 1):
                current_position_one = previous_row[num]
                current_position_two = previous_row[num + 1]
                matrix[row][counter] = current_position_one + current_position_two
                counter += 1

    return matrix

new_mat = [
           [1],
          [1, 1],
         [1, 2, 1],
        [1, 3, 3, 1],
       [1, 4, 6, 4, 1],
      [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1]
]

print(get_magic_triangle(5))