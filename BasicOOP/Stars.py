def first():
    x = 100
    def secon():
        nonlocal x
        x = 5

    print(x)
    secon()
    print(x)

first()