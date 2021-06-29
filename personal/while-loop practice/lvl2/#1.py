# Calculate the sum of digits of a number given by user. E.g.-
# INUPT : 123        OUPUT : 6
# INUPT : 12345        OUPUT : 15

print('Enter Q to quit!')
while True:
    total = 0
    try:
        num = input('Enter a string of numbers: ')
    except:
        print('You did not enter string of numbers! Try again.')
    else:
        if num.lower() == 'q':
            break
        for digit in num:
            total += int(digit)
        print(total)