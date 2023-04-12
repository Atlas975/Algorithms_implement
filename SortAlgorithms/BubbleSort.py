import random


def bubble_sort(data):  # O(n^2)
    n = len(data)
    for i in range(n):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


if __name__ == "__main__":
    data = random.sample(range(100), 10)
    print("Dataset: ", data)
    print(f"Bubble sort: {bubble_sort(data)}")
