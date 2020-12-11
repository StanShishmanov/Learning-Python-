n = int(input())
longest_intersection = set()

for i in range(n):
    ranges = input().split('-')
    first_range = [int(x) for x in ranges[0].split(',')]
    second_range = [int(x) for x in ranges[1].split(',')]
    first_set = set([x for x in range(first_range[0], first_range[1] + 1)])
    second_set = set([x for x in range(second_range[0], second_range[1] + 1)])
    intersection = first_set & second_set
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f'Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}')