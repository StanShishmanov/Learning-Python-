with open('test.txt', 'r') as file:
    lines = file.readlines()
    odd_lines = []

    for i in range(1, len(lines), 2):
        odd_lines.append(lines[i])

    with open('Output.txt', 'w') as output_file:
        output_file.writelines(odd_lines)
