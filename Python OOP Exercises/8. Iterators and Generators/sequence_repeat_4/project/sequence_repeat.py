class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.start = 0
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == len(self.sequence):
            self.start = 0

        if self.end < self.number:
            char = self.sequence[self.start]
            self.start += 1
            self.end += 1
            return char
        else:
            raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
