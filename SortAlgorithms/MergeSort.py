from typing import List, Union


def merge_sort(data):
    if len(data) == 1:
        return data
    split = len(data) // 2
    leftSegment = merge_sort(data[:split])
    rightSegment = merge_sort(data[split:])
    return merge_segement(leftSegment, rightSegment)


def merge_segement(leftSegment, rightSegment):
    result = []
    while leftSegment and rightSegment:
        if leftSegment[0] < rightSegment[0]:
            result.append(leftSegment.pop(0))
        else:
            result.append(rightSegment.pop(0))
    if leftSegment:
        result.extend(leftSegment)
    else:
        result.extend(rightSegment)
    return result


if __name__ == "__main__":
    import random

    data = random.sample(range(1000), 10)
    print(f"Dataset: {data}")
    print(f"Mergesort: {merge_sort(data)}")
