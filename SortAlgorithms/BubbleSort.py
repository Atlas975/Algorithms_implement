import numpy as np


def bubble_sort(data): # O(n^2)
    n = len(data)
    for _ in range(1, n):
        for j in range(n - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


data = np.random.randint(20, size=10)
print("Dataset: ", data)
print(f"Bubble sort: {bubble_sort(data)}")
