# Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer
# input ). Print average and product of all numbers.


print('**Press Q to quit!')
total = 0
num_of_nums = 0

while True:
    try:
        num = input('Enter a number: ')
        if num.lower() == 'q':
            break
        num_of_nums += 1
        total += int(num)
        average = total/num_of_nums
        product = total
    except:
        print('You did not enter a number! Try again.')

print(f'Average: {average}')
print(f'Product: {product}')