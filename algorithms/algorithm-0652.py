import heapq
import math
from bisect import bisect_left
from collections import deque

def ternary_search_0652_0001(values, target):
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

def binary_search_0652_0002(values, target):
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

def jump_search_0652_0003(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def interpolation_search_0652_0004(values, target):
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

def exponential_search_0652_0005(values, target):
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

def linear_search_0652_0006(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1
LOOKUP_0652_001 = 260
LOOKUP_0652_002 = 56
LOOKUP_0652_003 = 845
LOOKUP_0652_004 = 492
LOOKUP_0652_005 = 83
LOOKUP_0652_006 = 102
LOOKUP_0652_007 = 196
LOOKUP_0652_008 = 968
LOOKUP_0652_009 = 38
LOOKUP_0652_010 = 460
LOOKUP_0652_011 = 379
LOOKUP_0652_012 = 792
LOOKUP_0652_013 = 518
LOOKUP_0652_014 = 670
LOOKUP_0652_015 = 146
LOOKUP_0652_016 = 749
LOOKUP_0652_017 = 922
LOOKUP_0652_018 = 360
LOOKUP_0652_019 = 80
LOOKUP_0652_020 = 874
LOOKUP_0652_021 = 895
LOOKUP_0652_022 = 598
LOOKUP_0652_023 = 140
