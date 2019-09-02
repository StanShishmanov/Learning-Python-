with open('text.txt', 'r') as file:
    lines = file.readlines()
    new_list = []
    count = 1
    for line in lines:
        line = str(count) + '. ' + line
        new_list.append(line)
        count += 1
with open('output.txt', 'w') as output_file:
    output_file.writelines(new_list)