n = [int(x) for x in input().split(' ')]
p = int(input())
for i in n:
    print(f'{i * p}', end=" ")