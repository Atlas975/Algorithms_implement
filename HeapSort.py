
import numpy as np

def max_heap(data,n,root):
    new_root=root
    left=2*root+1
    right=2*root+2

    if left>=n: return data
    if data[left]>data[new_root]:
        new_root=left
    if right<n and data[right]>data[new_root]:
        new_root=right

    if new_root!=root:
        data[root],data[new_root]=data[new_root],data[root]
        data=max_heap(data,n,new_root)
    return data

def heap_sort(data):
    n=len(data)
    for parent in range(n//2-1,-1,-1):
        data=max_heap(data,n,parent)
    for i in range(n-1,0,-1):
        data[0],data[i]=data[i],data[0]
        data=max_heap(data,i,0)
    return data



data = np.random.randint(20, size = 10)
data = [9,6,9,0,1,3,2,9,7,2]
print(f"Dataset: {data}")
print(f"Heapsort: {heap_sort(data)}")

