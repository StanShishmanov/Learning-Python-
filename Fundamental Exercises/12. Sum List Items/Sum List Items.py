n = int(input())
my_list = []
for i in range(n):
    total = 0
    my_list += [int(input())]
for i in my_list:
    total += i
print(total)

