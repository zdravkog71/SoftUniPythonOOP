def type_check(t):
    def decorator(f):
        def wrapper(n):
            if type(n) == t:
                return f(n)
            else:
                return "Bad Type"
        return wrapper
    return decorator


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))