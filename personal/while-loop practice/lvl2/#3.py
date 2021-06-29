# Write a program to print a number given by user but digits reversed. E.g.-
# INPUT : 123        OUTPUT : 321
# INPUT : 12345        OUTPUT : 54321

print('Enter Q to quit!')
while True:
    reverse_num = []
    try:
        num = input('Enter a string of numbers: ')
    except:
        print('You did not enter string of numbers! Try again.')
    else:
        if num.lower() == 'q':
            break
        for i in num:
            reverse_num.insert(0, i)
        reverse_num = ''.join(reverse_num)
        print(reverse_num)