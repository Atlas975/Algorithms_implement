import numpy as np
from random import randrange


def bogo_sort(data):
    isSorted=True
    for i in range(len(data)-1):
        if(data[i]>data[i+1]):
            isSorted=False
    if isSorted:
        return data
    else:
        for i in range(len(data)):
            new_spot=randrange(len(data))
            data[i],data[new_spot]=data[new_spot],data[i]
    return bogo_sort(data)


# data = np.random.randint(20, size = 10)
# print(f"Dataset: {data}")
# print(f"Bogo sorted: {bogo_sort(data)}")

