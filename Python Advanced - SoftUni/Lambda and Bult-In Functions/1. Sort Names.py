def desc_sorter(my_list):
    return ' '.join(sorted(my_list, reverse=True))

print(desc_sorter(input().split()))