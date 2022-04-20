import random

def radix_sort(data):
    high = -float('inf')
    for value in data:
        if value > high:
            high = value
    num_digits = 0
    while (high > 0):
        high //= 10
        num_digits += 1

    for digit in range(num_digits):
        buckets = [[] for _ in range(10)]
        for value in data:
            bucket_index = (value // (10 ** digit)) % 10
            buckets[bucket_index].append(value)
        data=[values for bucket in buckets for values in bucket]
    return data

data=random.sample(range(1000),10)
print(f"Dataset: {data}")
print(f"Radix sort: {radix_sort(data)}")
