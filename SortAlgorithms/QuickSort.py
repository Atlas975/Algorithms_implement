def quicksort(data, l, r):
    if l < r:
        pidx = partition(data, l, r)
        quicksort(data, l, pidx - 1)
        quicksort(data, pidx + 1, r)
    return data


def partition(data, l, r):
    m = (l + r) // 2
    if data[m] > data[r]:
        data[m], data[r] = data[r], data[m]

    l, pivot = l, data[r]
    for i in range(l, r):
        if data[i] < pivot:  #
            data[l], data[i] = data[i], data[l]  # swap
            l += 1  # l is the index of the first element that is greater than pivot

    data[l], data[r] = data[r], data[l]  # r
    return l


if __name__ == "__main__":
    import random

    data = random.sample(range(1000), 10)
    print(f"Dataset: {data}")
    sorted_data = quicksort(data, 0, len(data) - 1)
    print(f"Quicksort: {sorted_data}")
