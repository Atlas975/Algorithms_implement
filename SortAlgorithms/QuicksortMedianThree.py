def quicksort(data, low, high):
    if low < high:
        p = partition(data, low, high)
        quicksort(data, low, p - 1)
        quicksort(data, p + 1, high)

    return data


def partition(data, low, high):
    mid = (low + high) // 2
    if data[mid] < data[low]:
        data[mid], data[low] = data[low], data[mid]
    if data[high] < data[low]:
        data[high], data[low] = data[low], data[high]
    if data[mid] < data[high]:
        data[mid], data[high] = data[high], data[mid]

    pivot = data[high]
    i = low
    for j in range(i, high):
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            i += 1
    data[i], data[high] = data[high], data[i]
    return i


if __name__ == "__main__":
    import random

    data = random.sample(range(1000), 10)
    print(f"Dataset: {data}")
    print(f"Quicksort: {quicksort(data,0,len(data)-1)}")
