import numpy as np

def bubble_sort(data):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if(data[j]>data[j+1]):
                data[j],data[j+1]=data[j+1],data[j]
    return data


data = np.random.randint(20, size = 10)
print("Dataset: ", data)
print(f"Bubble sort: {bubble_sort(data)}")
