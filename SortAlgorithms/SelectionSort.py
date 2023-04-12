import random


def selection_sort(data): # O(n^2)
    n = len(data)
    for i in range(n):
        low = i
        for j in range(i + 1, n):
            if data[j] < data[low]:
                low = j
        data[low], data[i] = data[i], data[low]


data = random.sample(range(1000), 10)
print(f"Dataset: {data}")
selection_sort(data)
print(f"Selection sort: {data}")
