# A three digit number is called Armstrong number if sum of cube of its digit is equal to number itself.
# E.g.- 153 is an Armstrong number because (1^3)+(5^3)+(3^3) = 153.
# Write all Armstrong numbers between 100 to 500.

values = {}
total = 0
for i in range(100, 501): # for every number
    for x in str(i): # every digit
        total += int(x)**3 # every seperate digit to cube and add sums
        if int(i) == total: # if the whole num is equal to cubic value of individual digits
            values[i] = total
    total = 0 # reset after every num check
print(values)