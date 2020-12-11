usernames = int(input())
names = set()
for i in range(usernames):
    names.add(input())
[print(name) for name in names]