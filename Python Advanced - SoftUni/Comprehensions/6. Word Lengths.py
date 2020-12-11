names = [name for name in input().split(', ')]

result = [name + ' -> ' + str(len(name)) for name in names]
print(', '.join(result))