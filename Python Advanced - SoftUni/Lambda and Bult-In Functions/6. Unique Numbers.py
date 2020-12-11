def unique_finder(input_list):
    rounds = [round(float(i)) for i in input_list]
    print(min(rounds))
    print(max(rounds))
    return ' '.join(map(str, sorted(set([int(i) * 3 for i in rounds]))))

print(unique_finder([float(i) for i in input().split()]))