import random


def bogo_sort(data):
    # if all(data[i]<=data[i+1] for i in range(n-1)):
    #     return data
    # for i in range(n):
    #     new_spot=random.randrange(n)
    #     data[i],data[new_spot]=data[new_spot],data[i]
    # return bogo_sort(data,n)
    n = len(data)
    iterations = 0
    while any(data[i] > data[i + 1] for i in range(n - 1)):
        for i in range(n):
            new_spot = random.randrange(n)
            data[i], data[new_spot] = data[new_spot], data[i]
        iterations += 1
    print(f"Number of iterations: {iterations}")
    return data


if __name__ == "__main__":
    data = random.sample(range(100), 10)
    print(f"Dataset: {data}")
    print(f"Bogo sorted: {bogo_sort(data)}")
