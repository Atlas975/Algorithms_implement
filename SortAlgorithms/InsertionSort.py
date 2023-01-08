import random
from typing import List


def insertion_sort(data): # O(n^2)
    for r in range(1, len(data)):
        l = r
        while l > 0 and data[l-1] > data[l]:
            data[l - 1], data[l] = data[l], data[l - 1]
            l -= 1


if __name__ == "__main__":
    data: List[float | int] = random.sample(range(100), 10)
    print(f"Dataset: {data}")
    insertion_sort(data)
    print(f"Insertion sort: {data}")
