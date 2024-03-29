from functools import reduce



def radix_sort(data):
    high = max(data)
    digcnt = 0
    while high > 0:
        high //= 10
        digcnt += 1

    for digit in range(digcnt):
        buckets = [[[] for _ in range(10)]]
        for value in data:
            bucket_index = (value // (10**digit)) % 10
            buckets[bucket_index].append(value)
        data = reduce(lambda x, y: x + y, buckets)
    return data


if __name__ == "__main__":
    data = random.sample(range(1000), 10)
    print(f"Dataset: {data}")
    print(f"Radix sort: {radix_sort(data)}")
