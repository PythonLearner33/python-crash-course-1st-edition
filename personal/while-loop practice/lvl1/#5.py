# Factorial of any number n is represented by n! and is equal to 1*2*3*....*(n-1)*n. E.g.-
# 4! = 1*2*3*4 = 24
# 3! = 3*2*1 = 6
# 2! = 2*1 = 2
# Also,
# 1! = 1
# 0! = 1
# Write a program to calculate factorial of a number.


while True:
    x = 1
    string = ''
    factorials = []
    num = input('Enter a number: ')
    if num == 0:
        print('0! = 1')
    if num == 1:
        print('1! = 1')
    else:
        for i in range(1, int(num)+1):
            x *= i
            factorials.append(i)
        for factorial in factorials:
            string += f'{factorial}*'
        string = string[:len(string)-1]
        print(f'{num}! = {string} = {x}\n')