# Take 10 integers from keyboard using loop and print their average value on the screen.
nums = []
required = 10
total = 0

while True:
    try:
        num = int(input(f'[{required} more required] Enter an integer: '))
    except:
        print('You did not enter an integer.')
    else:
        nums.append(num)
        required -= 1
        if len(nums) == 10:
            for x in nums:
                total += x
            print(f'\nAverage value: {int(total/10)}')
            break