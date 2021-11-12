primes= []
for prime in range(2,25):
    isPrime = True
    for num in range(2,prime):
        if prime % num == 0:
            isPrime=False
    if isPrime:
        primes.append(prime)
print(primes)


primes_Numbers = []
for p in range(2,50):
    isPrime = True
    for num in  range(2, p):
        if p % num == 0:
            isPrime = False
    if isPrime:
        primes_Numbers.append(p)
print(primes_Numbers)



