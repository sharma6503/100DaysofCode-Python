def prime_series(prime_range):
    for i in range(2, prime_range):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime:
            print(i, end=' ')


prime_range=int(input('Enter the range of prime numbers to be printed:'))

prime_series(prime_range)
