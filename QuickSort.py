import random

def quick_sort(data, low=0, high=None):

    if(high==None):
        high=len(data)-1
    if(low<high):
        pivot_idx = partition(data, low, high)
        quick_sort(data, low, pivot_idx-1)
        quick_sort(data, pivot_idx+1, high)
    return data

def partition(data,low,high):
    start=low
    if(data[high]<data[low]):
        data[high],data[low]=data[low],data[high]
        start+=1
        low+=1
    pivot=data[high]
    for i in range(low,high):
        if data[i]<=pivot:
            data[start],data[i]=data[i],data[start]
            start+=1
    data[start],data[high]=data[high],data[start]
    return start

data=random.sample(range(1000),10)
print(f"Dataset: {data}")
sorted_data=quick_sort(data,0,len(data)-1)
print(f"Quicksort: {sorted_data}")





