def solve(text, times):
    try:
        if not isinstance(times, int):
            raise TypeError('Variable times must be an integer')
        print(text * times)
    except TypeError as err:
        print(err)

solve('Pesho', '3')