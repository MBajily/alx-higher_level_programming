#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
dig = int(str(number)[-1:])
print(f'Last digit of {number:d} is {dig:d}', end=' ')
if dig > 5:
    print('and is greater than 5')
elif dig < 6:
    if dig == 0:
        print('and is 0')
    else:
        print('and is less than 6 and not 0')
