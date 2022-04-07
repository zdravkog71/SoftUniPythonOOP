class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current = 0
        self.counter = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter > self.count:
            raise StopIteration
        temp = self.current
        self.counter += 1
        self.current += self.step
        return temp




numbers = take_skip(10, 5)
for number in numbers:
    print(number)