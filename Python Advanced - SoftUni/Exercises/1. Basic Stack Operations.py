stack = []

nums = [int(x) for x in input().split()]
stack = [int(x) for x in input().split()]

for i in range(nums[1]):
    stack.pop()

if nums[2] in stack:
    print(True)
else:
    if len(stack) > 0:
        print(min(stack))
    else:
        print('0')