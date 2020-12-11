def func_executor(*args):
    new_list = []
    for arg in args:
        
        func = arg[0]
        params = arg[1]
        result = func(*params)
        new_list.append(result)

    return new_list