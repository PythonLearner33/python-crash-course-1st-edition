# Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of given two numbers.

while True:
    num, num2 = input('Enter numbers X Y: ').split(' ', 2)
    num1_factors, num2_factors = [], []

    for divisor in range(1, int(num)+1):
        x = int(num)/divisor # e.g. 12.0 
        x = str(x).split('.') # e.g. ['12', '0']
        if '0' in x: # Only allows for whole numbers; i.e. ['12', '48238'] = 12.48238
            num1_factors.append(int(x[0]))

    for divisor in range(1, int(num2)+1):
        y = int(num2)/divisor
        y = str(y).split('.')
        if '0' in y:
            num2_factors.append(int(y[0]))

    print(num1_factors)
    print(num2_factors)

    for GCF in num1_factors: # Checks for first match between lists and breaks. 
        if GCF in num2_factors:
            print(f'GCF: {GCF}\n')
            break