class take_skip:

    def __init__(self, step, count):
        self.start = 0
        self.step = step
        self.count = count
        self.total = self.step * self.count

    def __iter__(self):
        return self

    def __next__(self):
        current = self.start
        if self.start == 0:
            self.start += self.step
            return current
        else:
            if current < self.total:
                self.start += self.step
                return current
            else:
                raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
