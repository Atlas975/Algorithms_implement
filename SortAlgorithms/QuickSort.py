import random
import time


def quicksort(data, l, r):
    if l < r:
        pidx = partition(data, l, r)
        quicksort(data, l, pidx - 1)
        quicksort(data, pidx + 1, r)
    return data

def partition(data, l, r):
    pivot = data[r]
    for i in range(l, r):
        if data[i] < pivot:
            data[l], data[i] = data[i], data[l]
            l += 1
    data[l], data[r] = data[r], data[l]
    return l


def quicksort_custom(data, l, r):
    if l < r:
        pidx = partition_custom(data, l, r)
        quicksort_custom(data, l, pidx - 1)
        quicksort_custom(data, pidx + 1, r)
    return data


def partition_custom(data, l, r):
    m = (l + r) // 2
    if data[l] > data[r]:
        data[l], data[r] = data[r], data[l]
    if data[l] > data[m]:
        data[l], data[m] = data[m], data[l]
    if data[m] < data[r]:
        data[m], data[r] = data[r], data[m]

    pivot = data[r]
    for i in range(l, r):
        if data[i] < pivot:
            data[l], data[i] = data[i], data[l]
            l += 1
    data[l], data[r] = data[r], data[l]
    return l


if __name__ == "__main__":
    data = random.sample(range(100_000), 100_000)

    # time quicksort with regular pivot selection
    start = time.time()
    sorted_data = quicksort(data[:], 0, len(data) - 1)
    end = time.time()
    print(f"Time with regular pivot selection: {end - start:.6f} seconds")

    # time quicksort with median-of-three pivot selection
    start = time.time()
    sorted_data = quicksort_custom(data[:], 0, len(data) - 1)
    end = time.time()
    print(f"Time with custom pivot selection: {end - start:.6f} seconds")
