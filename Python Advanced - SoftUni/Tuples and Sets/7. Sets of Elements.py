lengths = input().split()
first = set()
second = set()
n = int(lengths[0])
m = int(lengths[1])
for i in range(n):
    first.add(int(input()))

for i in range(m):
    second.add(int(input()))
common = first & second
[print(x) for x in common]