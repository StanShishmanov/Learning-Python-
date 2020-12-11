lengths = [int(x) for x in input().split()]
n = lengths[0]
m = lengths[1]

first_set = set()
second_set = set()


for i in range(n):
    first_set.add(input())
for i in range(m):
    second_set.add(input())

inter_set = set.intersection(first_set, second_set)

for i in inter_set:
    print(i)