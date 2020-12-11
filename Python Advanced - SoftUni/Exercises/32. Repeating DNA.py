def get_repeating_DNA(*args):
    splitted_string = args[0]
    count = 10
    splitted_string = [splitted_string[i:i+count] for i in range(0, len(splitted_string), count)]
    total_strings = len(splitted_string)
    string_list = []
    repeating = set()
    

    for i in range(total_strings):
        if not isinstance(splitted_string, list):
            splitted_string = [''.join(splitted_string)]

        if len(splitted_string[0]) != 10:
            print(len(splitted_string[0]))
            if string_list:
                last = string_list[-1]
                difference = 10 - len(splitted_string[0])
                new_string = last[:difference]
                finished = new_string + splitted_string[0]
                if finished in string_list:
                    repeating.add(finished)
        else:
            if splitted_string[0] in string_list:
                repeating.add(splitted_string[0])
                splitted_string.pop(0)
            else:
                string_list.append(splitted_string[0])
                splitted_string.pop(0)
    return list(repeating)