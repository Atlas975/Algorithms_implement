def heapify(data, i, n):
    new_root = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and data[new_root] < data[l]:
        new_root = l
    if r < n and data[new_root] < data[r]:
        new_root = r
    if new_root != i:
        data[i], data[new_root] = data[new_root], data[i]
        heapify(data, new_root, n)


def heap_sort(data):
    n = len(data)
    for root in range(n // 2 - 1, -1, -1):
        heapify(data, root, n)

    for i in range(n - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        heapify(data, 0, i)


if __name__ == "__main__":
    import random

    data = random.sample(range(1000), 10)
    print(f"Dataset: {data}")
    heap_sort(data)
    print(f"Heapsort: {data}")
