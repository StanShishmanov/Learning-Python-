def separator(input_list):
    negatives = [i for i in input_list if i < 0]
    positives = [i for i in input_list if i > 0]

    print(f"-{abs(sum(negatives))}")
    print(sum(positives))
    if abs(sum(negatives)) > sum(positives):
        return f'The negatives are stronger than the positives'
    return f'The positives are stronger than the negatives'


print(separator([int(x) for x in input().split()]))