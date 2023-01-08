def quick_sort(data, l, r):
    if l < r:
        pivot_idx = partition(data, l, r)
        quick_sort(data, l, pivot_idx - 1)
        quick_sort(data, pivot_idx + 1, r)
    return data


def partition(data, low, high):
    mid = (low + high) // 2
    if data[mid] > data[high]:
        data[mid], data[high] = data[high], data[mid]

    l, pivot = low, data[high]
    for i in range(low, high):
        if data[i] < pivot:
            data[l], data[i] = data[i], data[l]
            l += 1

    data[l], data[high] = data[high], data[l]
    return l


if __name__ == "__main__":
    import random

    data = random.sample(range(1000), 10)
    print(f"Dataset: {data}")
    sorted_data = quick_sort(data, 0, len(data) - 1)
    print(f"Quicksort: {sorted_data}")
