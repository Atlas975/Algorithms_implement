import random
from math import floor
from DataTools.SortingClass import Sort as st


def binary_search(minIndex, maxIndex, target, data):
    if minIndex > maxIndex:
        return -1
    midIndex = (minIndex + maxIndex) // 2
    if target == data[midIndex]:
        return midIndex
    elif target < data[midIndex]:
        return binary_search(minIndex, midIndex - 1, target, data)
    else:
        return binary_search(midIndex + 1, maxIndex, target, data)


def binary_search_iter(target, data):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


data = list(range(20))
print(f"Dataset: {data}")


search1 = data[random.randint(0, len(data) - 1)]
search2 = data[random.randint(0, len(data) - 1)]
search3 = data[random.randint(0, len(data) - 1)]
print(
    f"Binary search for {search1}, found at index {binary_search(0,len(data)-1,search1,data)}"
)
print(
    f"Binary search for {search2}, found at index {binary_search(0,len(data)-1,search2,data)}"
)
print(
    f"Binary search for {search3}, found at index {binary_search(0,len(data)-1,search3,data)}"
)

print(f"Binary search for {search1}, found at index {binary_search_iter(search1,data)}")
