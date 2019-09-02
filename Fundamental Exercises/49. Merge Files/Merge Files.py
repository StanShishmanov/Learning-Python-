with open('input1.txt', 'r') as input1, open('input2.txt', 'r') as input2:
    first_input = input1.readlines()
    second_input = input2.readlines()
    new_list = []
    for i in first_input:
        i = i.strip('\n')
        new_list.append(i)
    for i in second_input:
        i = i.strip('\n')
        new_list.append(i)
with open('output.txt', 'w') as output_file:
    for i in new_list:
        output_file.writelines(i + '\n')
