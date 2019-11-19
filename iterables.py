from math import sqrt


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


primes = [x for x in range(101) if is_prime(x)]

print(primes)

words = "Some sentences have lots of words and some have little".split()

wordLengths = [len(word) for word in words]

print(wordLengths)


"""Block to test use of next on an iterator"""
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']

iterator = iter(seasons)

print(next(iterator))

print(next(iterator))

