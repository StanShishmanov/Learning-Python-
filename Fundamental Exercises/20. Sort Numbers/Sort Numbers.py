n = [int(i) for i in input().split()]
i = 0
counter = 0
while i < len(n):
    smallest = min(n[i:])
    index_of_smallest = n.index(smallest)
    n[i],n[index_of_smallest] = n[index_of_smallest],n[i]
    i=i+1
for i in n:
    if n[counter] > n[0]:
        print(f' <= {i}', end="")
    elif n[counter] == n[-1]:
        print(f'{i}', end=" ")
    else:
        print(f'{i}', end="")
    counter += 1

# 16 19 11 15 10 12 14