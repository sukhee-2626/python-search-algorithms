import heapq
import math
from bisect import bisect_left
from collections import deque

def linear_search_0496_0001(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def jump_search_0496_0002(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def ternary_search_0496_0003(values, target):
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

def exponential_search_0496_0004(values, target):
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

def binary_search_0496_0005(values, target):
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

def interpolation_search_0496_0006(values, target):
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

def interpolation_search_0496_0007(values, target):
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

def exponential_search_0496_0008(values, target):
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

def jump_search_0496_0009(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def binary_search_0496_0010(values, target):
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

def linear_search_0496_0011(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def ternary_search_0496_0012(values, target):
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

def linear_search_0496_0013(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def ternary_search_0496_0014(values, target):
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

def exponential_search_0496_0015(values, target):
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

def binary_search_0496_0016(values, target):
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

def interpolation_search_0496_0017(values, target):
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

def jump_search_0496_0018(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def linear_search_0496_0019(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def exponential_search_0496_0020(values, target):
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

def ternary_search_0496_0021(values, target):
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

def jump_search_0496_0022(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def interpolation_search_0496_0023(values, target):
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

def binary_search_0496_0024(values, target):
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

def interpolation_search_0496_0025(values, target):
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

def jump_search_0496_0026(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def linear_search_0496_0027(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def exponential_search_0496_0028(values, target):
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

def ternary_search_0496_0029(values, target):
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

def binary_search_0496_0030(values, target):
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

def binary_search_0496_0031(values, target):
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

def exponential_search_0496_0032(values, target):
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

def jump_search_0496_0033(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def linear_search_0496_0034(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def ternary_search_0496_0035(values, target):
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

def interpolation_search_0496_0036(values, target):
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

def ternary_search_0496_0037(values, target):
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

def interpolation_search_0496_0038(values, target):
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

def linear_search_0496_0039(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def jump_search_0496_0040(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def exponential_search_0496_0041(values, target):
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

def binary_search_0496_0042(values, target):
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

def interpolation_search_0496_0043(values, target):
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

def ternary_search_0496_0044(values, target):
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

def exponential_search_0496_0045(values, target):
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

def binary_search_0496_0046(values, target):
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

def jump_search_0496_0047(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def linear_search_0496_0048(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def linear_search_0496_0049(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def jump_search_0496_0050(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def interpolation_search_0496_0051(values, target):
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

def ternary_search_0496_0052(values, target):
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

def binary_search_0496_0053(values, target):
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

def exponential_search_0496_0054(values, target):
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

def linear_search_0496_0055(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def exponential_search_0496_0056(values, target):
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

def jump_search_0496_0057(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def interpolation_search_0496_0058(values, target):
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

def ternary_search_0496_0059(values, target):
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

def binary_search_0496_0060(values, target):
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

def exponential_search_0496_0061(values, target):
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

def interpolation_search_0496_0062(values, target):
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

def ternary_search_0496_0063(values, target):
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

def binary_search_0496_0064(values, target):
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

def linear_search_0496_0065(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def jump_search_0496_0066(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def jump_search_0496_0067(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def binary_search_0496_0068(values, target):
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

def exponential_search_0496_0069(values, target):
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

def linear_search_0496_0070(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def ternary_search_0496_0071(values, target):
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

def interpolation_search_0496_0072(values, target):
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

def interpolation_search_0496_0073(values, target):
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

def linear_search_0496_0074(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def exponential_search_0496_0075(values, target):
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

def jump_search_0496_0076(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def binary_search_0496_0077(values, target):
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

def ternary_search_0496_0078(values, target):
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

def binary_search_0496_0079(values, target):
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

def linear_search_0496_0080(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def jump_search_0496_0081(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def ternary_search_0496_0082(values, target):
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

def interpolation_search_0496_0083(values, target):
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

def exponential_search_0496_0084(values, target):
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

def interpolation_search_0496_0085(values, target):
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

def exponential_search_0496_0086(values, target):
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

def jump_search_0496_0087(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def ternary_search_0496_0088(values, target):
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

def linear_search_0496_0089(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def binary_search_0496_0090(values, target):
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

def jump_search_0496_0091(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def linear_search_0496_0092(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def interpolation_search_0496_0093(values, target):
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

def exponential_search_0496_0094(values, target):
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

def ternary_search_0496_0095(values, target):
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

def binary_search_0496_0096(values, target):
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

def interpolation_search_0496_0097(values, target):
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

def jump_search_0496_0098(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def ternary_search_0496_0099(values, target):
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

def linear_search_0496_0100(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def binary_search_0496_0101(values, target):
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

def exponential_search_0496_0102(values, target):
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

def ternary_search_0496_0103(values, target):
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

def linear_search_0496_0104(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def binary_search_0496_0105(values, target):
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

def exponential_search_0496_0106(values, target):
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

def jump_search_0496_0107(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def interpolation_search_0496_0108(values, target):
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

def ternary_search_0496_0109(values, target):
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

def jump_search_0496_0110(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def linear_search_0496_0111(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def binary_search_0496_0112(values, target):
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

def interpolation_search_0496_0113(values, target):
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

def exponential_search_0496_0114(values, target):
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

def linear_search_0496_0115(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def exponential_search_0496_0116(values, target):
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

def interpolation_search_0496_0117(values, target):
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

def ternary_search_0496_0118(values, target):
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

def binary_search_0496_0119(values, target):
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

def jump_search_0496_0120(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def interpolation_search_0496_0121(values, target):
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

def ternary_search_0496_0122(values, target):
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

def exponential_search_0496_0123(values, target):
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

def jump_search_0496_0124(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def binary_search_0496_0125(values, target):
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

def linear_search_0496_0126(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def ternary_search_0496_0127(values, target):
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

def linear_search_0496_0128(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def binary_search_0496_0129(values, target):
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

def jump_search_0496_0130(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def interpolation_search_0496_0131(values, target):
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

def exponential_search_0496_0132(values, target):
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

def ternary_search_0496_0133(values, target):
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

def interpolation_search_0496_0134(values, target):
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

def binary_search_0496_0135(values, target):
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

def jump_search_0496_0136(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def exponential_search_0496_0137(values, target):
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

def linear_search_0496_0138(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def exponential_search_0496_0139(values, target):
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

def jump_search_0496_0140(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def binary_search_0496_0141(values, target):
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

def ternary_search_0496_0142(values, target):
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

def interpolation_search_0496_0143(values, target):
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

def linear_search_0496_0144(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def exponential_search_0496_0145(values, target):
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

def jump_search_0496_0146(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def ternary_search_0496_0147(values, target):
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

def linear_search_0496_0148(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def binary_search_0496_0149(values, target):
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

def interpolation_search_0496_0150(values, target):
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

def interpolation_search_0496_0151(values, target):
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

def jump_search_0496_0152(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def linear_search_0496_0153(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def binary_search_0496_0154(values, target):
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

def ternary_search_0496_0155(values, target):
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

def exponential_search_0496_0156(values, target):
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

def exponential_search_0496_0157(values, target):
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

def binary_search_0496_0158(values, target):
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

def linear_search_0496_0159(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def ternary_search_0496_0160(values, target):
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

def jump_search_0496_0161(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def interpolation_search_0496_0162(values, target):
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

def binary_search_0496_0163(values, target):
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

def jump_search_0496_0164(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def exponential_search_0496_0165(values, target):
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

def interpolation_search_0496_0166(values, target):
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

def ternary_search_0496_0167(values, target):
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

def linear_search_0496_0168(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def ternary_search_0496_0169(values, target):
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

def jump_search_0496_0170(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def binary_search_0496_0171(values, target):
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

def linear_search_0496_0172(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def exponential_search_0496_0173(values, target):
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

def interpolation_search_0496_0174(values, target):
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

def ternary_search_0496_0175(values, target):
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

def binary_search_0496_0176(values, target):
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

def linear_search_0496_0177(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def jump_search_0496_0178(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def exponential_search_0496_0179(values, target):
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

def interpolation_search_0496_0180(values, target):
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

def linear_search_0496_0181(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def ternary_search_0496_0182(values, target):
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

def binary_search_0496_0183(values, target):
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

def jump_search_0496_0184(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def interpolation_search_0496_0185(values, target):
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

def exponential_search_0496_0186(values, target):
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

def linear_search_0496_0187(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def interpolation_search_0496_0188(values, target):
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

def exponential_search_0496_0189(values, target):
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

def ternary_search_0496_0190(values, target):
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

def binary_search_0496_0191(values, target):
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

def jump_search_0496_0192(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def binary_search_0496_0193(values, target):
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

def interpolation_search_0496_0194(values, target):
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

def linear_search_0496_0195(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def exponential_search_0496_0196(values, target):
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

def jump_search_0496_0197(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def ternary_search_0496_0198(values, target):
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

def jump_search_0496_0199(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def linear_search_0496_0200(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def interpolation_search_0496_0201(values, target):
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

def exponential_search_0496_0202(values, target):
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

def binary_search_0496_0203(values, target):
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

def ternary_search_0496_0204(values, target):
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

def exponential_search_0496_0205(values, target):
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

def linear_search_0496_0206(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def interpolation_search_0496_0207(values, target):
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

def binary_search_0496_0208(values, target):
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

def ternary_search_0496_0209(values, target):
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

def jump_search_0496_0210(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def binary_search_0496_0211(values, target):
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

def ternary_search_0496_0212(values, target):
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

def exponential_search_0496_0213(values, target):
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

def interpolation_search_0496_0214(values, target):
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

def jump_search_0496_0215(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def linear_search_0496_0216(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def ternary_search_0496_0217(values, target):
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

def binary_search_0496_0218(values, target):
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

def linear_search_0496_0219(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1
LOOKUP_0496_001 = 543
LOOKUP_0496_002 = 445
LOOKUP_0496_003 = 27
LOOKUP_0496_004 = 783
LOOKUP_0496_005 = 314
LOOKUP_0496_006 = 622
LOOKUP_0496_007 = 18
LOOKUP_0496_008 = 675
LOOKUP_0496_009 = 645
