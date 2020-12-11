def num_sorter(list_input):
    new_list = sorted([i for i in list_input if i.isdigit() and int(i) > len(list_input)])
    return ' '.join(new_list)
    
print(num_sorter(input().split()))