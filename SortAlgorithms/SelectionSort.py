import numpy as np
import random

def selection_sort(data):
    for i in range(len(data)):
        minimum = i
        for j in range(i+1, len(data)):
            if (data[j] < data[minimum]):
                minimum = j
        if(minimum != i):
            data[minimum], data[i] = data[i], data[minimum]
    return data

data=random.sample(range(1000),10)
print(f"Dataset: {data}")
print(f"Selection sort: {selection_sort(data)}")

