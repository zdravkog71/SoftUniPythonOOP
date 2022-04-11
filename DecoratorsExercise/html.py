def tags(tag):
    def decorator(f):

        def wrapper(*args):
            return f"<{tag}>{f(*args)}</{tag}>"
        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))