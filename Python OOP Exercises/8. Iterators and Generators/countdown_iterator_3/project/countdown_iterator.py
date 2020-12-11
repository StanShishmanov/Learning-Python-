class countdown_iterator:

    def __init__(self, count):
        self.count = count
        self.start = self.count

    def __iter__(self):
        return self

    def __next__(self):
        current_num = self.count
        if self.start == self.count:
            self.count -= 1
            return self.start
        else:
            if self.count >= 0:
                self.count -= 1
                return current_num
            else:
                raise StopIteration

iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
