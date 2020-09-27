def primes(n):
    if not hasattr(primes, 'd'):
        primes.d = {}
        primes.q = 2
        primes.primes = []
    if n < primes.q:
        return [p for p in primes.primes if p <= n]

    while True:
        if primes.q > n:
            return primes.primes
        if primes.q not in primes.d:
            primes.primes.append(primes.q)
            primes.d[primes.q * primes.q] = [primes.q]
        else:
            for p in primes.d[primes.q]:
                primes.d.setdefault(p + primes.q, []).append(p)
            del primes.d[primes.q]

        primes.q += 1
