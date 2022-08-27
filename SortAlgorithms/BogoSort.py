import numpy as np
from random import randrange


def bogo_sort(data):
    isSorted = all(data[i] <= data[i+1] for i in range(len(data)-1))
    if isSorted:
        return data
    for i in range(len(data)):
        new_spot=randrange(len(data))
        data[i],data[new_spot]=data[new_spot],data[i]
    return bogo_sort(data)


if __name__ == '__main__':
    data = np.random.randint(10, size = 4)
    print(f"Dataset: {data}")
    print(f"Bogo sorted: {bogo_sort(data)}")

