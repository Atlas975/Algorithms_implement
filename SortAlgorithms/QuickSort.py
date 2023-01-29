def quick_sort(data, l, r):
    if l < r:
        pidx = partition(data, l, r)
        quick_sort(data, l, pidx - 1)
        quick_sort(data, pidx + 1, r)
    return data


def partition(data, l, r):
    m = (l + r) // 2
    if data[m] > data[r]:
        data[m], data[r] = data[r], data[m]

    l, pivot = l, data[r]
    for i in range(l, r):
        if data[i] < pivot:
            data[l], data[i] = data[i], data[l]
            l += 1

    data[l], data[r] = data[r], data[l]
    return l


if __name__ == "__main__":
    import random

    data = random.sample(range(1000), 10)
    print(f"Dataset: {data}")
    sorted_data = quick_sort(data, 0, len(data) - 1)
    print(f"Quicksort: {sorted_data}")
