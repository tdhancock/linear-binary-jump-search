import pytest
from random import seed, sample
from time import perf_counter
from math import sqrt
import time

def linear_search(lyst, target):
    i = 0
    while i < len(lyst):
        if lyst[i] == target:
            return True
        i += 1
    return False

def binary_search(lyst, target):
    if len(lyst) <= 1:
        if lyst[0] == target:
            return True
    else:
        midpoint = len(lyst) //2
        if lyst[midpoint] == target:
            return True
        elif target < lyst[midpoint]:
            return binary_search(lyst[:midpoint], target)
        else: 
            return binary_search(lyst[midpoint:], target)
    return False

def jump_search(lyst, target):
    strLen = len(lyst)
    step = int(sqrt(strLen))
    last = 0

    while lyst[(min(step, strLen) -1)] < target:
        last = step
        step += step
        if last >= strLen:
            return False
    
    while lyst[last] <= target:
        if lyst[last] == target:
            return True
        last += 1

def make_data():
    DATA_SIZE = 1000000
    seed(0)
    data = sample(range(DATA_SIZE * 3), k=DATA_SIZE)
    data.sort()
    while True:
        return data

def main():

    data = make_data()
    data.sort()
    DATA_SIZE = len(data)

    start = perf_counter()
    linear_search(data, data[0])
    end = perf_counter() - start
    print(f"Linear Search Time first element: {end} seconds")

    start = perf_counter()
    binary_search(data, data[0])
    end = perf_counter() - start
    print(f"Binary Search Time first element: {end} seconds")

    start = perf_counter()
    jump_search(data, data[0])
    end = perf_counter() - start
    print(f"Jump Search Time first element: {end} seconds\n")

    start = perf_counter()
    linear_search(data, data[(DATA_SIZE // 2) - 1])
    end = perf_counter() - start
    print(f"Linear Search Time middle element: {end} seconds")

    start = perf_counter()
    binary_search(data, data[(DATA_SIZE // 2) - 1])
    end = perf_counter() - start
    print(f"Binary Search Time middle element: {end} seconds")

    start = perf_counter()
    jump_search(data, data[(DATA_SIZE // 2) - 1])
    end = perf_counter() - start
    print(f"Jump Search Time middle element: {end} seconds\n")

    start = perf_counter()
    linear_search(data, data[-1])
    end = perf_counter() - start
    print(f"Linear Search Time final element: {end} seconds")

    start = perf_counter()
    binary_search(data, data[-1])
    end = perf_counter() - start
    print(f"Binary Search Time final element: {end} seconds")

    start = perf_counter()
    jump_search(data, data[-1])
    end = perf_counter() - start
    print(f"Jump Search Time final element: {end} seconds\n")

    start = perf_counter()
    linear_search(data, -1)
    end = perf_counter() - start
    print(f"Linear Search Time element not in list: {end} seconds")

    start = perf_counter()
    binary_search(data, -1)
    end = perf_counter() - start
    print(f"Binary Search Time element not in list: {end} seconds")

    start = perf_counter()
    jump_search(data, -1)
    end = perf_counter() - start
    print(f"Jump Search Time element not in list: {end} seconds\n")

if __name__ == "__main__":
    main()