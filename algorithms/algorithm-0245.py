import heapq
import math
from bisect import bisect_left
from collections import deque

def interpolation_search_0245_0001(values, target):
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

def jump_search_0245_0002(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def exponential_search_0245_0003(values, target):
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

def linear_search_0245_0004(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def binary_search_0245_0005(values, target):
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

def ternary_search_0245_0006(values, target):
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

def interpolation_search_0245_0007(values, target):
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

def binary_search_0245_0008(values, target):
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

def jump_search_0245_0009(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def linear_search_0245_0010(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def ternary_search_0245_0011(values, target):
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

def exponential_search_0245_0012(values, target):
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

def interpolation_search_0245_0013(values, target):
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

def binary_search_0245_0014(values, target):
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

def ternary_search_0245_0015(values, target):
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

def exponential_search_0245_0016(values, target):
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

def linear_search_0245_0017(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def jump_search_0245_0018(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def linear_search_0245_0019(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def ternary_search_0245_0020(values, target):
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

def jump_search_0245_0021(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def binary_search_0245_0022(values, target):
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

def interpolation_search_0245_0023(values, target):
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

def exponential_search_0245_0024(values, target):
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

def ternary_search_0245_0025(values, target):
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

def binary_search_0245_0026(values, target):
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

def jump_search_0245_0027(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def linear_search_0245_0028(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def interpolation_search_0245_0029(values, target):
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

def exponential_search_0245_0030(values, target):
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

def binary_search_0245_0031(values, target):
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

def exponential_search_0245_0032(values, target):
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

def interpolation_search_0245_0033(values, target):
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

def linear_search_0245_0034(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def ternary_search_0245_0035(values, target):
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

def jump_search_0245_0036(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def linear_search_0245_0037(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def jump_search_0245_0038(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def exponential_search_0245_0039(values, target):
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

def binary_search_0245_0040(values, target):
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

def interpolation_search_0245_0041(values, target):
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

def ternary_search_0245_0042(values, target):
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

def jump_search_0245_0043(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def interpolation_search_0245_0044(values, target):
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

def linear_search_0245_0045(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def ternary_search_0245_0046(values, target):
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

def binary_search_0245_0047(values, target):
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

def exponential_search_0245_0048(values, target):
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

def ternary_search_0245_0049(values, target):
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

def interpolation_search_0245_0050(values, target):
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

def linear_search_0245_0051(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def jump_search_0245_0052(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def binary_search_0245_0053(values, target):
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

def exponential_search_0245_0054(values, target):
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

def jump_search_0245_0055(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def linear_search_0245_0056(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def interpolation_search_0245_0057(values, target):
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

def exponential_search_0245_0058(values, target):
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

def ternary_search_0245_0059(values, target):
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

def binary_search_0245_0060(values, target):
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

def exponential_search_0245_0061(values, target):
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

def ternary_search_0245_0062(values, target):
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

def jump_search_0245_0063(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def binary_search_0245_0064(values, target):
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

def linear_search_0245_0065(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def interpolation_search_0245_0066(values, target):
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

def ternary_search_0245_0067(values, target):
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

def exponential_search_0245_0068(values, target):
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

def linear_search_0245_0069(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def interpolation_search_0245_0070(values, target):
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

def binary_search_0245_0071(values, target):
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

def jump_search_0245_0072(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def jump_search_0245_0073(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def linear_search_0245_0074(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def interpolation_search_0245_0075(values, target):
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

def binary_search_0245_0076(values, target):
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

def exponential_search_0245_0077(values, target):
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

def ternary_search_0245_0078(values, target):
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

def exponential_search_0245_0079(values, target):
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

def binary_search_0245_0080(values, target):
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

def interpolation_search_0245_0081(values, target):
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

def ternary_search_0245_0082(values, target):
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

def jump_search_0245_0083(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def linear_search_0245_0084(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def interpolation_search_0245_0085(values, target):
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

def linear_search_0245_0086(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def jump_search_0245_0087(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def exponential_search_0245_0088(values, target):
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

def ternary_search_0245_0089(values, target):
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

def binary_search_0245_0090(values, target):
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

def ternary_search_0245_0091(values, target):
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

def jump_search_0245_0092(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def binary_search_0245_0093(values, target):
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

def exponential_search_0245_0094(values, target):
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

def linear_search_0245_0095(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def interpolation_search_0245_0096(values, target):
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

def exponential_search_0245_0097(values, target):
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

def ternary_search_0245_0098(values, target):
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

def linear_search_0245_0099(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def binary_search_0245_0100(values, target):
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

def jump_search_0245_0101(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def interpolation_search_0245_0102(values, target):
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

def interpolation_search_0245_0103(values, target):
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

def linear_search_0245_0104(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def ternary_search_0245_0105(values, target):
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

def exponential_search_0245_0106(values, target):
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

def binary_search_0245_0107(values, target):
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

def jump_search_0245_0108(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def jump_search_0245_0109(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def interpolation_search_0245_0110(values, target):
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

def binary_search_0245_0111(values, target):
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
LOOKUP_0245_001 = 466
LOOKUP_0245_002 = 777
LOOKUP_0245_003 = 207
LOOKUP_0245_004 = 279
LOOKUP_0245_005 = 278
LOOKUP_0245_006 = 81
LOOKUP_0245_007 = 338
LOOKUP_0245_008 = 151
LOOKUP_0245_009 = 726
LOOKUP_0245_010 = 548
LOOKUP_0245_011 = 833
LOOKUP_0245_012 = 358
LOOKUP_0245_013 = 235
LOOKUP_0245_014 = 478
LOOKUP_0245_015 = 401
