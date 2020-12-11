def fibonacci():
    num = 0
    yield num
    num += 1
    yield num
    yield num
    current = num
    yield current + num
    num += current

    while True:
        last = current
        yield num + current
        current = num
        num += last


generator = fibonacci()
for i in range(10):
    print(next(generator))
