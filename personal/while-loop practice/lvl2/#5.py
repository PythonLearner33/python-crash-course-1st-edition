# Write a program to print all prime number in between 1 to 100.

factors = {}
primes = []
for i in range(1, 100+1):
    factors[i]=[]
    for x in range(1, i+1):
        factor = float(i / x)
        if str(factor).split('.')[1]=='0':
            factors[i].append(factor)

    if len(factors[i]) <= 2:
        primes.append(int(factors[i][0]))

print(primes)