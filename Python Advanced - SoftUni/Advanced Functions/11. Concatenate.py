def concatenate(*args):
    new_string = ''
    for i in args:
        new_string += i
    return new_string

print(concatenate("Soft", "Uni", "Is", "Great", "!"))