from collections import deque
open_parentheses = ['{', '[', '(', ' ']
closed_parentheses = ['}', ']', ')', ' ']
even = True
parentheses = deque(str(x) for x in input())

while parentheses:
    opening = parentheses.popleft()
    closing = parentheses.pop()
    if not open_parentheses.index(opening) == closed_parentheses.index(closing):
        even = False
        print('NO')
        break
if even:
    print("YES")