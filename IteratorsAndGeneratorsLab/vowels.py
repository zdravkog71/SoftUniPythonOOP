class vowels:
    def __init__(self, text):
        self.text = text
        self.all_vowels = "AEIOUYaeiuoy"
        self.vowel_lsit = [el for el in self.text if el in self.all_vowels]
        self.start = 0
        self.end = len(self.vowel_lsit) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        index = self.start
        self.start += 1
        return self.vowel_lsit[index]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)