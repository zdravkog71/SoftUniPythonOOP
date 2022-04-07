def is_prime(num):
    is_prime = True
    if num == 1 or num == 0:
        is_prime = False
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
    return is_prime

def get_primes(seq):

    for num in seq:
        if is_prime(num):
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))


