class dictionary_iter:
    def __init__(self, dic):
        self.dic = dic
        self.elements = list(self.dic.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.elements):
            raise StopIteration
        temp_index = self.index
        self.index += 1
        return self.elements[temp_index]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)