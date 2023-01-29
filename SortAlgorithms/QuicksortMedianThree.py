def quicksort(data, low, high):
    if low < high:
        p = partition(data, low, high)
        quicksort(data, low, p - 1)
        quicksort(data, p + 1, high)

    return data


def partition(data, l, r):
    m = (l + r) // 2
    if data[r] < data[l]:
        data[r], data[l] = data[l], data[r]
    if data[m] < data[l]:
        data[m], data[l] = data[l], data[m]
    elif data[r] < data[m]:
        data[r], data[m] = data[m], data[r]

    pivot = data[r]
    i = l
    for j in range(i, r):
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            i += 1
    data[i], data[r] = data[r], data[i]
    return i


if __name__ == "__main__":
    import random

    data = random.sample(range(1000), 10)
    print(f"Dataset: {data}")
    print(f"Quicksort: {quicksort(data,0,len(data)-1)}")
