#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
dig = int(str(number)[-1:])
if dig > 5:
    print(f'Last digit of {number:d} is {dig:d} and is greater than 5')
elif dig < 6:
    if dig == 0:
        print(f'Last digit of {number:d} is {dig:d} and is 0')
    else:
        print(f'Last digit of {number:d} is {dig:d} and is less than 6 and not 0')
