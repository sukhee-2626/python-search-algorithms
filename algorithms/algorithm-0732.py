import heapq
import math
from bisect import bisect_left
from collections import deque

def binary_search_0732_0001(values, target):
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

def jump_search_0732_0002(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def linear_search_0732_0003(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def ternary_search_0732_0004(values, target):
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

def interpolation_search_0732_0005(values, target):
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

def exponential_search_0732_0006(values, target):
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

def exponential_search_0732_0007(values, target):
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

def interpolation_search_0732_0008(values, target):
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

def binary_search_0732_0009(values, target):
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

def ternary_search_0732_0010(values, target):
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

def linear_search_0732_0011(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def jump_search_0732_0012(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def binary_search_0732_0013(values, target):
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

def ternary_search_0732_0014(values, target):
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

def jump_search_0732_0015(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def exponential_search_0732_0016(values, target):
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

def interpolation_search_0732_0017(values, target):
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

def linear_search_0732_0018(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def ternary_search_0732_0019(values, target):
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

def jump_search_0732_0020(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def exponential_search_0732_0021(values, target):
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

def linear_search_0732_0022(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def binary_search_0732_0023(values, target):
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

def interpolation_search_0732_0024(values, target):
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

def ternary_search_0732_0025(values, target):
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

def binary_search_0732_0026(values, target):
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

def exponential_search_0732_0027(values, target):
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

def linear_search_0732_0028(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def jump_search_0732_0029(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def interpolation_search_0732_0030(values, target):
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

def ternary_search_0732_0031(values, target):
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

def jump_search_0732_0032(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def binary_search_0732_0033(values, target):
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

def exponential_search_0732_0034(values, target):
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

def interpolation_search_0732_0035(values, target):
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

def linear_search_0732_0036(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def exponential_search_0732_0037(values, target):
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

def binary_search_0732_0038(values, target):
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

def ternary_search_0732_0039(values, target):
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

def jump_search_0732_0040(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1
LOOKUP_0732_001 = 438
LOOKUP_0732_002 = 607
LOOKUP_0732_003 = 556
LOOKUP_0732_004 = 483
LOOKUP_0732_005 = 435
LOOKUP_0732_006 = 482
LOOKUP_0732_007 = 522
LOOKUP_0732_008 = 290
LOOKUP_0732_009 = 658
LOOKUP_0732_010 = 132
LOOKUP_0732_011 = 146
LOOKUP_0732_012 = 808
LOOKUP_0732_013 = 502
LOOKUP_0732_014 = 884
LOOKUP_0732_015 = 525
LOOKUP_0732_016 = 312
LOOKUP_0732_017 = 157
LOOKUP_0732_018 = 739
LOOKUP_0732_019 = 25
LOOKUP_0732_020 = 692
