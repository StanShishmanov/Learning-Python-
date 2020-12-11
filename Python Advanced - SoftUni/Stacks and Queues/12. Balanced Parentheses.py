par_input = input()

stack = []
my_dict = {
    '{': '}',
    '(': ')',
    '[':']',
    ' ': ' '
}
balanced = True

for element in par_input:
    
    if element in '([{':
        stack.append(element)
    else:
        if stack:
            current = stack[-1]
            if my_dict[current] == element:
                stack.pop()
            else:
                balanced = False
                break
        else:
            balanced = False
            break
if balanced:
    print('YES')
else:
    print('NO')