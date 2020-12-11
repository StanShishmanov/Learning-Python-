n = int(input())

longest = []

for i in range(n):
    line = input()
    first_start = int(line.split('-')[0].split(',')[0])
    first_end = int(line.split('-')[0].split(',')[1])
    second_start = int(line.split('-')[1].split(',')[0])
    second_end = int(line.split('-')[1].split(',')[1])

    full_start = max(first_start, second_start)
    full_end = min(first_end, second_end)
    new_longest = []
    for i in range(full_start, full_end + 1):
        new_longest.append(i)
    if len(new_longest) > len(longest):
        longest = new_longest

print(f"Longest intersection is {longest} with length {len(longest)}")