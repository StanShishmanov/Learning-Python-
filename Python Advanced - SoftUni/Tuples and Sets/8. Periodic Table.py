n = int(input())
elements_list = []

for i in range(n):
    elements = input().split()
    [elements_list.append(element) for element in elements]

elements_set = set(elements_list)
[print(x) for x in elements_set]