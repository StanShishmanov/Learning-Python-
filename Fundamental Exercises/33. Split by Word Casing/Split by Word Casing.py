import re
input_string = [i for i in re.split("[,;:.!()\'\"\\\\/[\] ]+", input()) if i != ""]
lower_list = []
upper_list = []
mixed_list = []

for word in input_string:

    if word.islower():
        case_checker = True
        for i in word:
            if 97 <= ord(i) <= 122:
                case_checker = True
            else:
                case_checker = False
                break
        if case_checker:
            lower_list.append(word)
        else:
            mixed_list.append(word)

    elif word.isupper():
        case_checker = True
        for i in word:
            if 65 <= ord(i) <= 90:
                case_checker = True
            else:
                case_checker = False
                break
        if case_checker:
            upper_list.append(word)
        else:
            mixed_list.append(word)

    else:
        mixed_list.append(word)
print(f'Lower-case: {", ".join(map(str, lower_list))}')
print(f'Mixed-case: {", ".join(map(str, mixed_list))}')
print(f'Upper-case: {", ".join(map(str, upper_list))}')

# Learn programming at SoftUni: Java, PHP, JS, HTML 5, CSS, Web, C#, SQL, databases, AJAX, etc.