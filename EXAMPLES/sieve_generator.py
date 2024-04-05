
def next_prime(limit):
    already_seen = set()  # initialize empty set (to be used for "is-prime" flags

    for i in range(2, limit):
        if i in already_seen:
            continue
        for j in range(2 * i, limit + 1, i):
            already_seen.add(j)  # add non-prime elements to set
        yield i  # execution stops here until next value is requested by for-in loop


np = next_prime(20000)  # next_prime() returns a generator object
for prime in np:  # iterate over yielded primes
    print(prime, end=' ')
