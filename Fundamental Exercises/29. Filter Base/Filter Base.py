age_dict = {}
position_dict = {}
salary_dict = {}
can_input = True
while can_input:
    line = input().split(' -> ')
    if line[0] == "filter base":
        can_input = False
        break
    else:
        if "." in line[1]:
            try:
                val = float(line[1])
                salary_dict[line[0]] = val
            except ValueError:
                print("No.. the input string is not a float. It's a string or an int")
        elif line[1].isdigit():
            val = int(line[1])
            age_dict[line[0]] = val
        else:
            position_dict[line[0]] = line[1]


def printer(n):
    if n == "Age":
        for k, v in age_dict.items():
            print(f'Name: {k}')
            print(f'Age: {v}')
            print('====================')
    elif n == "Position":
        for k, v in position_dict.items():
            print(f'Name: {k}')
            print(f'Position: {v}')
            print('====================')
    elif n == "Salary":
        for k, v in salary_dict.items():
            print(f'Name: {k}')
            print(f'Salary: {v}')
            print('====================')
last_input = input()
printer(last_input)