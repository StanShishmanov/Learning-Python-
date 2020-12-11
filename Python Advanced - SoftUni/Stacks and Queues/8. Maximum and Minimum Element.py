def solve():
    nums = int(input())
    i = 0
    stack = []
    while i < nums:
        i += 1
        new_input = input().split()
        command = int(new_input[0])

        if command == 1:
            stack.append(int(new_input[1]))
        elif command == 2:
            if stack:
                stack.pop()
            else:
                continue
        elif command == 3:
            if stack:
                print(max(stack))
            else:
                continue
        elif command == 4:
            if stack:
                print(min(stack))
            else:
                continue
    print(*stack[::-1], sep=', ')

solve()