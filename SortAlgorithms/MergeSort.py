
from typing import List, Union


def merge_sort(data: List[Union[int, float]]):
    if(len(data)==1): return data
    split=len(data)//2
    leftSegment=data[:split]
    rightSegment=data[split:]
    leftSegment=merge_sort(leftSegment)
    rightSegment=merge_sort(rightSegment)
    return merge_segement(leftSegment,rightSegment)

def merge_segement(leftSegment: List[Union[int, float]], rightSegment: List[Union[int, float]]):
    result = []
    while leftSegment and rightSegment:
        if leftSegment[0] < rightSegment[0]:
            result.append(leftSegment[0])
            leftSegment.pop(0)
        else:
            result.append(rightSegment[0])
            rightSegment.pop(0)
    if leftSegment:
        result.extend(leftSegment)
    else:
        result.extend(rightSegment)
    return result


if __name__=="__main__":
    import random
    data=random.sample(range(1000),10)
    print(f"Dataset: {data}")
    print(f"Mergesort: {merge_sort(data)}")


