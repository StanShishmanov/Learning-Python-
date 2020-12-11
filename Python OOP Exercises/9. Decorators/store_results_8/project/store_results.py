class store_results:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        name = self.func.__name__

        result = self.func(*args)
        return f"Function '{name}' was called. Result: {result}"



@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

print(add(2, 2))
print(mult(6, 4))
