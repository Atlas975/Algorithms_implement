import random


def bogo_sort(data):
    n = len(data)
    while any(data[i] > data[i + 1] for i in range(n - 1)):
        for i in range(n):
            new_spot = random.randrange(n)
            data[i], data[new_spot] = data[new_spot], data[i]
    return data


if __name__ == "__main__":
    data = random.sample(range(100), 10)
    print(f"Dataset: {data}")
    print(f"Bogo sorted: {bogo_sort(data)}")
