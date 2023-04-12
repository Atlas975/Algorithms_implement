def quicksort(data, low, high):
    if low < high:
        p = partition(data, low, high)
        quicksort(data, low, p - 1)
        quicksort(data, p + 1, high)
    return data


def partition(data, l, r):
    m = (l + r) // 2   
    if data[l] > data[r]:
        data[l], data[r] = data[r], data[l]
    if data[l] > data[m]:
        data[l], data[m] = data[m], data[l]
    if data[m] < data[r]:
        data[m], data[r] = data[r], data[m]
        
    pivot = data[r]
    for i in range(l, r):
        if data[i] < pivot:  
            data[l], data[i] = data[i], data[l]  
            l += 1  
    data[l], data[r] = data[r], data[l]  
    return l


if __name__ == "__main__":
    import random
    data = random.sample(range(1000), 10)
    print(f"Dataset: {data}")
    print(f"Quicksort: {quicksort(data,0,len(data)-1)}")
