import sys

from IPython.core import ultratb
sys.excepthook=ultratb.FormattedTB(mode='Verbose', color_scheme='Linux', call_pdb=False)
import random

def radix_sort(data):
    high = max(data)
    num_digits = 0
    while (high > 0):
        high //= 10
        num_digits += 1

    for digit in range(num_digits):
        buckets = [[[] for _ in range(10)]]
        for value in data:
            bucket_index = (value // (10 ** digit)) % 10
            buckets[bucket_index].append(value)
        data=[values for bucket in buckets for values in bucket]
    return data


if __name__=="__main__":
    data=random.sample(range(1000),10)
    print(f"Dataset: {data}")
    print(f"Radix sort: {radix_sort(data)}")
