class reverse_iter:
    def __init__(self, iter_obj):
        self.iter_obj = iter_obj
        self.start = len(self.iter_obj) - 1
        self.end = 0


    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            raise StopIteration
        index = self.start
        self.start -= 1
        return self.iter_obj[index]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)