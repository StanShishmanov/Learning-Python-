my_string = [x.strip(' ') for x in input().split("|")]
my_string = my_string[::-1]
my_string = [i.replace(",", "") for i in my_string]
new_list = []
for i in my_string:
    if i != " ":
        new_list.append(i)
for i in new_list:
    print(f'{" ".join(i.split())}', end= " ")