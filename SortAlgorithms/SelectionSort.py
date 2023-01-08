import random


def selection_sort(data):
    n = len(data)
    for i in range(n):
        minimum = i
        for j in range(i + 1, n):
            if data[j] < data[minimum]:
                minimum = j
        if minimum != i:
            data[minimum], data[i] = data[i], data[minimum]


data = random.sample(range(1000), 10)
print(f"Dataset: {data}")
selection_sort(data)
print(f"Selection sort: {data}")
