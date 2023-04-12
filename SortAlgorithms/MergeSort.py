def merge_sort(data): # O(n log n) time O(n) space 
    if len(data) < 2:
        return data
    split = len(data) // 2
    left = merge_sort(data[:split])
    right = merge_sort(data[split:])
    return merge_segement(left, right, data)

def merge_segement(left, right, data):
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1
    for i, num in enumerate(left[i:]):
        data[k] = num
        k += 1
    for j, num in enumerate(right[j:]):
        data[k] = num
        k += 1
    return data


if __name__ == "__main__":
    import random
    data = random.sample(range(1000), 10)
    print(f"Dataset: {data}")
    print(f"Merge sort: {merge_sort(data)}")