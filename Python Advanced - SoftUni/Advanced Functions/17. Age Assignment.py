def age_assignment(*args, **kwargs):
    names_dict = {}
    for key in kwargs:
        for name in args:
            if key == name[0]:
                names_dict[name] = kwargs[key]
    return names_dict

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))