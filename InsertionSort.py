import random

def insertion_sort(data):
    for i in range(1,len(data)):
        minimum=i
        for j in range(i-1,-1,-1):
            if (data[j]>data[minimum]):
                data[j],data[minimum]=data[minimum],data[j]
                minimum-=1
            else:
                break
    return data


data=random.sample(range(1000),10)
print(f"Dataset: {data}")
print(f"Insertion sort: {insertion_sort(data)}")


