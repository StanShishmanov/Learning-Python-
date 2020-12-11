class Fibonacci:

    def __init__(self):
        self.cache = {}

    def __call__(self, n):
        if n not in self.cache:
            if n == 0:
                self.cache[0] = 0
            elif n == 1:
                self.cache[1] = 1
            else:
                previous = self(n-1)
                current = self(n-2)
                self.cache[n] = previous + current
        return self.cache[n]


fib = Fibonacci()
for i in range(10):
    print(fib(i))
print(fib.cache)