# Write a program to find prime factor of a number.
# If a factor of a number is prime number then it is its prime factor.

print('Enter Q to quit!')
while True:
    factors = []
    prime_factors = {}
    try:
        num = input('Enter a number: ')
    except:
        print('You did not enter a number! Try again.')
    else:
        if num.lower() == 'q':
            break
        num = int(num)
        for x in range(1, num+1):
            factor = str(num / x).split('.')
            if factor[1] == '0':
                factors.append(factor[0])
        
        for factor in factors:
            prime_factors[factor]=[]
            for x in range(1, int(factor)+1):
                prime_factor = str(int(factor)/x).split('.')
                if prime_factor[1]=='0':
                    prime_factors[factor].append(prime_factor[0])
                
        for num in prime_factors:
            if len(prime_factors[num]) == 2:
                print(prime_factors[num][0])