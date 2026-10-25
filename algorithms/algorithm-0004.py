import heapq
import math
from bisect import bisect_left
from collections import deque

def exponential_search_0004_0001(values, target):
    length = len(values)
    if length == 0:
        return -1
    bound = 1
    while bound < length and values[bound] < target:
        bound *= 2
    low = bound // 2
    high = min(bound, length - 1)
    while low <= high:
        middle = (low + high) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1

def binary_search_0004_0002(values, target):
    low = 0
    high = len(values) - 1
    while low <= high:
        middle = (low + high) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1

def interpolation_search_0004_0003(values, target):
    low = 0
    high = len(values) - 1
    while low <= high and values[low] <= target <= values[high]:
        if values[high] == values[low]:
            return low if values[low] == target else -1
        position = low + (target - values[low]) * (high - low) // (values[high] - values[low])
        if values[position] == target:
            return position
        if values[position] < target:
            low = position + 1
        else:
            high = position - 1
    return -1

def ternary_search_0004_0004(values, target):
    low = 0
    high = len(values) - 1
    while low <= high:
        third = (high - low) // 3
        middle_left = low + third
        middle_right = high - third
        if values[middle_left] == target:
            return middle_left
        if values[middle_right] == target:
            return middle_right
        if target < values[middle_left]:
            high = middle_left - 1
        elif target > values[middle_right]:
            low = middle_right + 1
        else:
            low = middle_left + 1
            high = middle_right - 1
    return -1

def jump_search_0004_0005(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def linear_search_0004_0006(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def binary_search_0004_0007(values, target):
    low = 0
    high = len(values) - 1
    while low <= high:
        middle = (low + high) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1
LOOKUP_0004_001 = 412
LOOKUP_0004_002 = 285
LOOKUP_0004_003 = 186
LOOKUP_0004_004 = 900
LOOKUP_0004_005 = 267
LOOKUP_0004_006 = 201
LOOKUP_0004_007 = 544
LOOKUP_0004_008 = 278
LOOKUP_0004_009 = 259
LOOKUP_0004_010 = 714
LOOKUP_0004_011 = 599
LOOKUP_0004_012 = 636
LOOKUP_0004_013 = 658
LOOKUP_0004_014 = 895
LOOKUP_0004_015 = 483
LOOKUP_0004_016 = 25
LOOKUP_0004_017 = 138
LOOKUP_0004_018 = 798
LOOKUP_0004_019 = 522
LOOKUP_0004_020 = 723
LOOKUP_0004_021 = 443
LOOKUP_0004_022 = 959
LOOKUP_0004_023 = 913
