def logged(func):
    def wrapper(*args):
        name = func.__name__
        result = func(*args)
        return f"you called {name}{args}\nit returned {result}"
    return wrapper


@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))
