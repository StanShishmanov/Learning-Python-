my_list = [int(i) for i in input().split(" ")]
counter = 0
for i in my_list:
    if i % 2 != 0:
        counter += 1
print(counter)