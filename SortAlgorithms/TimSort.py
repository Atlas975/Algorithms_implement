MIN_MERGE = 64


def timsort(data):
    if len(data) < 2:
        return data
    mid = len(data) // 2
    left = timsort(data[:mid])
    right = timsort(data[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]


if __name__ == "__main__":
    import random

    data = random.sample(range(1000), 10)
    print(f"Dataset: {data}")
    print(f"Tim sort: {timsort(data)}")
