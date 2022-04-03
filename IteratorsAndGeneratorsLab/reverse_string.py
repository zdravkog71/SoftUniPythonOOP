def reverse_text(text):
    n = len(text) - 1
    while n >= 0:
        yield text[n]
        n -= 1

for char in reverse_text("step"):
    print(char, end='')