from math import floor
expression = input().split()
full_expression = []

operators = []
for i in expression:
    try:
        full_expression.append(int(i))
    except ValueError:
        operators.append(i)
        full_expression.append(i)
        
while operators:
    i = operators[0]
    indexed_operator = full_expression.index(i)
    if i == '-':
        new_list = full_expression[: indexed_operator]
            
        for elem in range(len(new_list)):
            if len(new_list) > 1:
                result = new_list[0] - new_list[1]
                new_list[0] = result
                new_list.pop(1)
        
        full_expression = new_list + full_expression[indexed_operator + 1:]
        operators.pop(0)

    elif i == '*':
        new_list = full_expression[: indexed_operator]
            
        for elem in range(len(new_list)):
            if len(new_list) > 1:
                result = new_list[0] * new_list[1]
                new_list[0] = result
                new_list.pop(1)
        
        full_expression = new_list + full_expression[indexed_operator + 1:]
        operators.pop(0)

    elif i == '/':
        new_list = full_expression[: indexed_operator]

        for elem in range(len(new_list)):
            if len(new_list) > 1:
                result = floor(new_list[0] / new_list[1])
                new_list[0] = result
                new_list.pop(1)
        
        full_expression = new_list + full_expression[indexed_operator + 1:]
        operators.pop(0)
    elif i == '+':
        result = 0
        new_list = full_expression[: indexed_operator]

        for elem in range(len(new_list)):
            if len(new_list) > 1:
                result = new_list[0] + new_list[1]
                new_list[0] = result
                new_list.pop(1)
        
        full_expression = new_list + full_expression[indexed_operator + 1:]
        operators.pop(0)

print(full_expression[0])