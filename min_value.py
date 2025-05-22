#!/usr/bin/env python3

# Created By: Luke Di Bert
# Date: May 20, 2025

# adds random module
import random


def min_value(array):
    min_value = 100
    for counter in range(0, len(array)):
        if array[counter] < min_value:
            min_value = array[counter]
    return min_value


def main():
    rand_num_array = []
    for counter in range(0, 10):
        rand_num_array.append(random.randint(0, 100))
        print(rand_num_array[counter], "was added to the array")
    minimum_value = min_value(rand_num_array)
    print("The minimum value is", minimum_value)


if __name__ == "__main__":
    main()
