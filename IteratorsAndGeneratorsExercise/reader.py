def read_next(*args):
    for colection in args:
        for item in colection:
            yield item

for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')