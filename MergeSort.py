import random

def merge_sort(data):
    if(len(data)==1):
        return data
    split=round(len(data)/2)
    leftSegment=data[:split]
    rightSegment=data[split:]
    leftSegment=merge_sort(leftSegment)
    rightSegment=merge_sort(rightSegment)
    return merge_segement(leftSegment,rightSegment)

def merge_segement(leftSegment,rightSegment):
    result=[]
    while(len(leftSegment)>0 and len(rightSegment)>0):
        if(leftSegment[0]<rightSegment[0]):
            result.append(leftSegment[0])
            leftSegment.pop(0)
        else:
            result.append(rightSegment[0])
            rightSegment.pop(0)
    if(len(leftSegment)!=0):
        result.extend(leftSegment)
    else:
        result.extend(rightSegment)
    return result


data=random.sample(range(1000),10)
print(f"Dataset: {data}")
print(f"Mergesort: {merge_sort(data)}")


