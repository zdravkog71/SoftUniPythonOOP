def even_parameters(f):
    def wrapper(*args):
        msg_to_return = "Please use only even numbers!"
        try:
            for arg in args:
                if not arg % 2 == 0:
                    return msg_to_return
            result = f(*args)
            return result
        except:
            return msg_to_return
    return wrapper

@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))