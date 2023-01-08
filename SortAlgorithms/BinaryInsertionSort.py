def binarySearch(a, item, low, high):
    while low <= high:
        mid = (high + low) // 2
        if item == a[mid]:
            return mid + 1
        elif item > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return low


def insertionSort(data):
    for i in range(1, len(data)):
        j = i - 1
        target = data[i]
        loc = binarySearch(data, data[i], 0, high=j)
        while j >= loc:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = target
        # data = data[:j] + [data[i]] + data[j:i] + data[i+1:]  alternative method to insert item in sorted array
    return data


if __name__ == "__main__":
    import random

    data = random.sample(range(1000), 10)
    print(f"Dataset: {data}")
    print(f"Tim sort: {insertionSort(data)}")


# def binarySearch_recur(data, target, low=0, high=0):
#     if low == high:
#         return low if data[low] > target else low + 1
#     if low > high:
#         return low
#     mid = (low + high) // 2
#     if target == data[mid]:
#         return mid
#     if target < data[mid]:
#         return binarySearch(data, target, low, mid - 1)
#     return binarySearch(data, target, mid + 1, high)
