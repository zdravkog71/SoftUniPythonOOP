class sequence_repeat:
    def __init__(self, seq, number):
        self.seq = seq
        self.number = number
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.number:
            raise StopIteration
        index = self.counter % len(self.seq)
        self.counter += 1
        return self.seq[index]

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')