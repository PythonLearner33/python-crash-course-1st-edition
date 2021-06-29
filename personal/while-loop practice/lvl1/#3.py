# Print multiplication table of 24, 50 and 29 using loop.

nums = [24, 50, 29]
for num in nums:
    i = 1
    print('') #extra blank line
    while i <= 10:
        print(f'{i}*{num} = {i*num}')
        i +=1