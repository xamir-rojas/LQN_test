"""
Part 1- Logic Excersice
"""
import numpy as np


def numbers():
    """
    - Prints numbers from 0 to 100
    - Prints buzz in same line when number is even
    - Prints bazz in same line when number is a multiple of 5 
    """
    numbers_array = np.arange(0, 101)
    for number in numbers_array:
        if(np.mod(number, 10) == 0):
            # Multiples of 10 are the common multiplies of 2 and 5.
            print(number, " buzz  bazz")
        elif(np.mod(number, 5) == 0):
            print(number, " bazz")
        elif(np.mod(number, 2) == 0):
            print(number, " buzz")
        else:
            print(number)


if __name__ == "__main__":
    numbers()
