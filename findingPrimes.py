def allPrimesUpTo(num):
    primes = [2]
    for number in range(2, num):
        sqrt = number ** 0.5
        for factor in primes:
            if number % factor == 0:
                break
            if factor > sqrt:
                primes.append(number)
                break
    return primes

print(allPrimesUpTo(10))