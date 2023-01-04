"""
Tanner Hancock
CS2420
Project 1
9/14/21
"""
from math import sqrt

def linear_search(lyst, target):
    """
    Do a Linear Search
    """
    i = 0
    while i < len(lyst):
        if lyst[i] == target:
            return True
        i += 1
    return False

def binary_search(lyst, target):
    """
    Do a Binary Search
    """
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
    """
    Do a Jump Search
    """
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
