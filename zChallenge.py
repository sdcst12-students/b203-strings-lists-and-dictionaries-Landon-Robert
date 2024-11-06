#!python3
# Explain what this code does

import random
x = []
for i in range(40):
    if random.randint(0,1):
        x.append(random.randint(1,10))
    else:
        x.append(random.randint(1,10) + random.randint(1,10)/10)

print(x)


"""
First, it generates a random number. If the number is 0 or 1 it generates a number between 1 and 10 and appends it to the list "x". If the number is not 0 or 1, it generates a number betwen 1 and 10 and adds it to a number between 1 and 10 divided by 10 (making it a 10's decimal) and adds that to the list "x". It goes through this process 40 times.
"""

