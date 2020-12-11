def solve(values):
    occurences = {}
    for v in values:
        if v not in occurences:
            occurences[v] = 0
        
        occurences[v] += 1

    for k, v in occurences.items():
        print(f'{k} - {v} times')

values_str = input().split(' ')
values = [float(x) for x in values_str]
solve(values)