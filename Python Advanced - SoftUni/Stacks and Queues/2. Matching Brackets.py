def matching_brackets(expression):
    open_brackets = []
    sub_exp = []

    for i in range(len(expression)):
        char = expression[i]
        if char == '(':
            open_brackets.append(i)
        elif char == ')':
            start = open_brackets.pop()
            end = i
            sub_exp.append(expression[start : end + 1])
    return sub_exp
    
expression = '1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5'
sub_expressions = matching_brackets(expression)
[print(subs) for subs in sub_expressions]