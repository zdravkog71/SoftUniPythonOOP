def vowel_filter(function):
    def wrapper():
        chars = function()
        vowels = [ch for ch in chars if ch.lower() in "aeiouy"]
        return vowels
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())