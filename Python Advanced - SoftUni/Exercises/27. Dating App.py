from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])
matches = 0


while True:
    if not males:
        break
    elif not females:
        break
    else:
        woman = females[0]
        man = males[-1]
        if woman <= 0:
            females.popleft()
        elif man <= 0:
            males.pop()

        elif man == woman:
            females.popleft()
            males.pop()
            matches += 1

        elif woman % 25 == 0:
            females.popleft()
            females.popleft()

        elif man % 25 == 0:
            males.pop()
            males.pop()

        else:
            females.popleft()
            males[-1] -= 2

print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join(reversed([str(x) for x in males]))}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join([str(x) for x in females])}")
else:
    print("Females left: none")