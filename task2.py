#!python3

'''
use a for loop to iterate through all possible integers to find the factors of 24
'''
def main():
    factors = []
    myNumber = 24
    for i in range(myNumber):
        if i != 0 and myNumber/i == int(myNumber/i):
            factors.append(i)
    print(factors)

if __name__ == "__main__":
    main()